import math
from typing import Optional, Tuple, Union

import logging
import numpy as np
import torch
import warnings

from dynaphos.cortex_models import get_cortical_magnification
from dynaphos.image_processing import scale_image, to_n_dim
from dynaphos.utils import (to_tensor, get_data_kwargs, get_truncated_normal,
                            get_deg2pix_coeff, set_deterministic,
                            print_stats, sigmoid, to_numpy, Map)

class State:
    def __init__(self, params: dict, shape: Tuple[int, ...],
                 verbose: Optional[bool] = False):
        self.params = params
        self.shape = shape
        self.verbose = verbose
        self.state = None
        self.data_kwargs = get_data_kwargs(self.params)

        self.reset()

    def reset(self):
        self.state = torch.zeros(self.shape, **self.data_kwargs)

    def get(self) -> torch.Tensor:
        return self.state

    def update(self, x: torch.Tensor):
        raise NotImplementedError

    def to_tensor(self, x: np.ndarray) -> torch.Tensor:
        return to_tensor(x, **self.data_kwargs)


class Activation(State):
    def __init__(self, params: dict, shape: Tuple[int, ...],
                 verbose: Optional[bool] = False):
        super().__init__(params, shape, verbose)

        self.fps = self.to_tensor(self.params['run']['fps'])
        # By default, the stimulus lasts as long as a frame. Can be adjusted:
        self.rel_stim_duration = self.to_tensor(
            self.params['default_stim']['relative_stim_duration'])
        # Convert decay-per-second to exponential decay constant.
        self.decay_rate = -torch.log(self.to_tensor(
            self.params['temporal_dynamics']['activation_decay_per_second']))
        self.num_steps = int(torch.ceil(self.decay_rate / self.fps))

    def update(self, x: torch.Tensor):
        """Update activation with leaky integrator.

        :param x: Effective stimulation current.
        """

        # If decay rate > frame rate, perform extra simulation steps for
        # numerical stability.
        for _ in range(self.num_steps):
            # eq: \Delta A = (-\gamma * A + I) * \Delta t
            self.state = self.state.detach() + (
                (-self.state.detach() * self.decay_rate + x * self.rel_stim_duration) /
                self.fps / self.num_steps)

        print_stats('activation', self.state, self.verbose)

class ActivationThreshold(State):
    def __init__(self, params: dict, shape: Tuple[int, ...],
                 rng: np.random.Generator, verbose: Optional[bool] = False):
        super().__init__(params, shape, verbose)
        self.rng = rng
        self._mu = self.params['thresholding']['activation_threshold']
        self._sd = self.params['thresholding']['activation_threshold_sd']
        self.reinitialize()

    def reinitialize(self, activation_thresholds: Optional[np.ndarray] = None):
        """Set or re-initialize the activation thresholds for each electrode. Default: sample from truncated random
        normal distribution."""
        if self.params['thresholding']['use_threshold']:
            if activation_thresholds is None:
                activation_thresholds = self.rng.standard_normal(self.shape) * self._sd + self._mu
            self.state = self.to_tensor(activation_thresholds).clip(0, None)
        else:
            self.state = torch.zeros(self.shape, **self.data_kwargs)

class Trace(State):
    def __init__(self, params: dict, shape: Tuple[int, ...],
                 verbose: Optional[bool] = False):
        super().__init__(params, shape, verbose)

        fps = self.params['run']['fps']

        # By default, the stimulus lasts as long as a frame. Can be adjusted:
        rel_stim_duration = \
            self.params['default_stim']['relative_stim_duration']

        # Convert decay-per-second to exponential decay constant.
        decay_rate = -math.log(
            self.params['temporal_dynamics']['trace_decay_per_second'])

        # Scaling of the trace increment.
        scale = self.params['temporal_dynamics']['trace_increase_rate']

        # If decay rate > frame rate, perform extra simulation steps for
        # numerical stability.
        self.num_steps = math.ceil(decay_rate / fps)

        self._a = self.to_tensor(-decay_rate / fps / self.num_steps)
        self._b = self.to_tensor(rel_stim_duration * scale / fps /
                                 self.num_steps)

    def update(self, x: torch.Tensor):
        """Update memory trace using a leaky integrator.

        :param x: Effective stimulation current.
        """
        for _ in range(self.num_steps):
            self.state = self.state.detach() + self._a * self.state.detach() + self._b * x

        print_stats('trace', self.state, self.verbose)


class Brightness(State):
    def __init__(self, params: dict, shape: Tuple[int, ...], verbose: Optional[bool] = False):
        super().__init__(params, shape, verbose)
        self.slope = self.to_tensor(
            self.params['brightness_saturation']['slope_brightness'])
        self.cps_half = self.to_tensor(
            self.params['brightness_saturation']['cps_half'])

    def update(self, x: torch.Tensor):
        """Saturate activation values."""

        self.state = sigmoid(self.slope * (x - self.cps_half))
        print_stats('sigmoided activation', self.state, self.verbose)


class Sigma(State):
    def __init__(self, params: dict, shape: Tuple[int, ...],
                 magnification: torch.Tensor, verbose: Optional[bool] = False):
        super().__init__(params, shape, verbose)

        p = self.params['size']
        if p['size_equation'] == 'sqrt':  # Tehovnik 2007
            def f(x):
                return torch.sqrt(torch.div(x, p['current_spread']))
        elif p['size_equation'] == 'sigmoid':  # Bosking et al., 2017
            def f(x):
                return 0.5 * p['MD'] * sigmoid(p['slope_size'] *
                                               (x - p['I_half']))
        else:
            raise ValueError("Size equation should be 'sqrt' or 'sigmoid'.")
        self.f = f
        self.scale = p['radius_to_sigma'] / magnification
    def update(self, x: torch.Tensor):
        """Compute the effect of the input current on phosphene size."""

        # Current spread to sigma in pixels.
        self.state = torch.mul(self.f(x), self.scale)

        print_stats('Sigma (in degrees)', self.state, self.verbose)


class GaussianSimulator:
    def __init__(self, params: dict, coordinates: Map,
                 rng: Optional[np.random.Generator] = None, 
                 theta: Optional[np.ndarray] = None):
        """initialize a simulator with provided parameters settings,
        given phosphene locations in polar coordinates

        :param params: dict of dicts with all setting parameters.
        :param coordinates: Eccentricities and angles of phosphenes.
        :param theta: Orientations for gabor filtering (if 'gabor_filtering' set to True)
        :param rng: Numpy random number generator.
        """

        self.params = params
        self.data_kwargs = get_data_kwargs(self.params)

        rng = np.random.default_rng() if rng is None else rng
        set_deterministic(self.params['run']['seed'])

        self.deg2pix_coeff = get_deg2pix_coeff(self.params['run'])

        self.phosphene_maps = \
            self.generate_phosphene_maps(coordinates, theta=theta)

        batch_size = self.params['run']['batch_size']
        if batch_size != 0:
            self.shape = (batch_size, self.num_phosphenes, 1, 1)
            self._electrode_dimension = 1
        else:
            self.shape = (self.num_phosphenes, 1, 1)
            self._electrode_dimension = 0

        r, phi = coordinates.polar
        r = torch.reshape(self.to_tensor(r), self.shape[-3:])
        self.magnification = get_cortical_magnification(
            r, self.params['cortex_model'])

        verbose = self.params['run']['print_stats']
        self.activation = Activation(params, self.shape, verbose=verbose)
        self.trace = Trace(params, self.shape)
        self.sigma = Sigma(params, self.shape, self.magnification)
        self.brightness = Brightness(params, self.shape)
        self.threshold = ActivationThreshold(params, self.shape, rng)
        self.effective_charge_per_second = None

        # Pre-allocate some helper variables.
        self._sampling_mask = None
        self._phosphene_centers = None
        params_sampling = self.params['sampling']
        self._sampling_method = params_sampling['sampling_method']
        self._sqrt_pi_inv = 1 / torch.sqrt(self.to_tensor(torch.pi))
        self._pulse_width = (self.params['default_stim']['pw_default'] *
                             torch.ones(self.shape, **self.data_kwargs))
        self._frequency = (self.params['default_stim']['freq_default'] *
                           torch.ones(self.shape, **self.data_kwargs))

        self._zero = self.to_tensor(0)
        self._inf = self.to_tensor(torch.inf)

        self.reset()

    @property
    def num_phosphenes(self):
        return len(self.phosphene_maps)

    def to_tensor(self, x: Union[int, float, np.ndarray]) -> torch.Tensor:
        return to_tensor(x, **self.data_kwargs)

    def reset(self):
        """Reset Memory of previous timestep."""
        self.activation.reset()
        self.trace.reset()
        self.sigma.reset()

    def gabor_rotation(self, x, y, theta=None) -> torch.Tensor:
        """Rotation of ellipsis."""
        num_phosphenes = len(x)
        if theta is None:
            theta = torch.mul(2 * math.pi, torch.rand((num_phosphenes, 1, 1), **self.data_kwargs)) # Random rotation
        else:
            theta = torch.reshape(self.to_tensor(theta), (-1, 1, 1))
        y_rotated = -x * torch.sin(theta) + y * torch.cos(theta)
        x_rotated = x * torch.cos(theta) + y * torch.sin(theta)
        gamma = self.params['gabor']['gamma']
        phosphene_maps = torch.sqrt(x_rotated ** 2 + y_rotated ** 2 * gamma ** 2)
        return phosphene_maps

    def generate_phosphene_maps(self, coordinates: Map,
                                remove_invalid: Optional[bool] = True,
                                theta: Optional[np.ndarray] = None,
                                ) -> torch.Tensor:
        """Generate phosphene maps (for each phosphene distance to each pixel).

        :param coordinates: Coordinates of phosphenes.
        :param remove_invalid: Whether to remove phosphenes out of view.
        :param theta: Orientations for gabor filtering (if 'gabor_filtering' set to True)
        :return: an (n_phosphenes x resolution[0] x resolution[1]) array
        describing distances from phosphene locations
        """

        # Phosphene coordinates
        x_coords, y_coords = coordinates.cartesian
        x_coords = torch.reshape(self.to_tensor(x_coords), (-1, 1, 1))
        y_coords = torch.reshape(self.to_tensor(y_coords), (-1, 1, 1))

        # x,y limits of the simulation
        res_x, res_y = self.params['run']['resolution']
        x_org, y_org = self.params['run']['origin']
        hemi_fov = self.params['run']['view_angle'] / 2
        x_min, x_max = x_org - hemi_fov, x_org + hemi_fov
        y_min, y_max = y_org - hemi_fov, y_org + hemi_fov
     
        if remove_invalid:
            # Check if phosphene locations are inside of view angle.
            valid = (
                torch.ge(x_coords, x_min) & torch.less(x_coords, x_max) &
                torch.ge(y_coords, y_min) & torch.less(y_coords, y_max)).ravel()
            num_total = len(x_coords)
            num_valid = torch.sum(valid)
            logging.debug(f"{num_total - num_valid} of {num_total} phosphenes "
                          f"are outside of view and will be removed.")
            x_coords = x_coords[valid]
            y_coords = y_coords[valid]
            coordinates.use_subset(to_numpy(valid))

        # Get distance maps to phosphene centres (in degrees of visual angle).
        device = self.data_kwargs['device']
        num_phosphenes = len(x_coords)

        x_range = torch.linspace(x_min, x_max, res_x, device=device)
        y_range = torch.linspace(y_min, y_max, res_y, device=device)

        grid = torch.meshgrid(x_range, y_range, indexing='xy')
        grid_x = torch.tile(grid[0], (num_phosphenes, 1, 1))
        grid_y = torch.tile(grid[1], (num_phosphenes, 1, 1))
        x = grid_x - x_coords
        y = grid_y - y_coords

        if self.params['gabor']['gabor_filtering']:
            phosphene_maps = self.gabor_rotation(x, y, theta)
        else:
            phosphene_maps = torch.sqrt(x ** 2 + y ** 2)

        return phosphene_maps

    def update(self, amplitude: torch.Tensor,
               pulse_width: Optional[torch.Tensor] = None,
               frequency: Optional[torch.Tensor] = None):
        """Update phosphene states (brightness, size, tissue activation) as
        function of the electrical stimulation input and the previous state.

        :param amplitude: Stimulation amplitudes for each electrode.
        :param pulse_width: Stimulation pulse widths for each electrode.
        :param frequency: Stimulation frequencies for each electrode.
        """

        if pulse_width is None:
            pulse_width = self._pulse_width
        if frequency is None:
            frequency = self._frequency

        charge_per_s = self.get_current(amplitude.view(self.shape),
                                        frequency.view(self.shape),
                                        pulse_width.view(self.shape))

        self.activation.update(charge_per_s)

        self.trace.update(charge_per_s)

        self.sigma.update(amplitude.view(self.shape))

        self.brightness.update(self.activation.get())

    def get_current(self, amplitude: torch.Tensor, frequency: torch.Tensor,
                    pulse_width: torch.Tensor) -> torch.Tensor:
        """Caclulate effective current (charge per second) from the square wave
        pulse. Cannot be negative.

        :param amplitude: Stimulation amplitudes for each electrode.
        :param pulse_width: Stimulation pulse widths for each electrode.
        :param frequency: Stimulation frequencies for each electrode.
        """

        leak_current = \
            self.trace.get() + self.params['thresholding']['rheobase']
        charge_per_s = torch.relu((amplitude - leak_current) *
                                  pulse_width * frequency)
        self.effective_charge_per_second = charge_per_s

        print_stats('charge per second', charge_per_s)

        return charge_per_s

    def gaussian_activation(self) -> torch.Tensor:
        """Generate gaussian activation maps, based on sigmas and phosphene
        mapping.

        :return: Stack of Gaussian-shaped phosphene images
        (n_phosphenes, resolution_y, resolution_x)
        """

        # Calculate normalized Gaussian (peak has value 1).
        sigma = self.sigma.get().clamp(1e-22, None)  # TODO: clamping redundant? Default division by zero gives inf.
        exp = torch.exp(-0.5 * (self.phosphene_maps / sigma) ** 2)
        return exp

    def get_state(self):
        state = {
            'brightness': self.brightness.get(),
            'sigma': self.sigma.get(),
            'activation': self.activation.get(),
            'trace': self.trace.get(),
            'threshold': self.threshold.get(),
            'effective_charge_per_second':
                self.effective_charge_per_second}
        return state

    def __call__(self, amplitude: torch.Tensor,
                 pulse_width: Optional[torch.Tensor] = None,
                 frequency: Optional[torch.Tensor] = None) -> torch.Tensor:
        """Generate simulated phosphene representation based on the
        electrical stimulation parameters and the previous state.

        :param amplitude: Stimulation amplitudes for each electrode.
        :param pulse_width: Stimulation pulse widths for each electrode.
        :param frequency: Stimulation frequencies for each electrode.

        :return: image with simulated phosphene representation
        """

        # Update phosphene state.
        self.update(amplitude, pulse_width, frequency)

        # Generate phosphene map.
        activation = self.gaussian_activation()

        # Thresholding: Set phosphene intensity to zero if tissue activation is lower than threshold.
        supra_threshold = torch.greater(self.activation.get(), self.threshold.get())
        intensity = torch.where(supra_threshold, self.brightness.get(), self._zero)

        # Return phosphene image.
        return torch.sum(intensity * activation, dim=self._electrode_dimension).clamp(0, 1)

    @property
    def phosphene_centers(self):
        """Indices (flat indexing) of the phosphene centers"""
        if self._phosphene_centers is None:
            self._phosphene_centers = self.phosphene_maps.flatten(start_dim=1).argmin(dim=-1)
        return self._phosphene_centers

    def sample_centers(self, x: torch.Tensor) -> torch.Tensor:
        """Extracts the value of the activation mask at the center pixel of each phosphene"""
        # instead of multiplying with sampling mask, values are retrieved using the indices of the center pixels
        return x.flatten(-2)[..., self.phosphene_centers]

    def sample_receptive_fields(self, x: torch.Tensor) -> torch.Tensor:
        """Extracts the maximum value of activation mask x within the 'receptive field' of each phosphene"""
        return torch.amax(self.sampling_mask * x, dim=(-2,-1))

    @property
    def sampling_mask(self):
        """Boolean mask (tensor) that defines which pixels are inside the receptive field / center of each phosphene"""
        if self._sampling_mask is None:
            params = self.params['sampling']
            if self._sampling_method == 'receptive_fields':
                self._sampling_mask = torch.less(self.phosphene_maps, params['RF_size'] / self.magnification)
            elif self._sampling_method == 'center':
                # Sampling mask is not used anymore in 'center' mode (pixels are directly retrieved using indexing),
                # but still implemented here for backwards compatibility
                p_map = self.phosphene_maps
                flat_idx = torch.arange(p_map.shape[0], device=p_map.device) * p_map.shape[-2] * p_map.shape[-1]
                self._sampling_mask = torch.zeros_like(p_map)
                self._sampling_mask.flatten()[self.phosphene_centers + flat_idx] = 1
            else:
                raise NotImplementedError
        return self._sampling_mask

    def sample_stimulus(self, activation_mask: Union[np.ndarray, torch.Tensor], rescale=False,
                        ) -> torch.Tensor:
        """Obtain a stimulation vector from an activation mask image that indicates the regional stimulation intensity.

        param activation_mask: Image (or batch of images: N, 1, H, W). The pixel intensities indicate the
                                stimulation amplitude for each visual region.

        param rescale: If False (default), the pixel intensities indicate the stimulation amplitude in Amperes.
                        If True, the input pixels (in range [0, 1] or [0, 255]) are mapped to stimulation amplitudes
                        using the default stimulus scale parameter specified in the params configuration file.

        return: Stimulation tensor with the stimulation amplitudes for each phosphene. """

        if isinstance(activation_mask, np.ndarray):
            dtype = activation_mask.dtype
            activation_mask = self.to_tensor(activation_mask)
            if (dtype == np.dtype('uint8')) or (activation_mask.max() > 1):
                activation_mask = scale_image(activation_mask, 1 / 255)
        if self._sampling_method == 'receptive_fields':
            electrode_activation = self.sample_receptive_fields(activation_mask)
        elif self._sampling_method == 'center':
            electrode_activation = self.sample_centers(activation_mask)  # electrode activations between 0 and 1
        else:
            raise NotImplementedError
        if rescale:
            electrode_activation = torch.mul(electrode_activation, self.params['sampling']['stimulus_scale'])
        elif electrode_activation.max() >= 1e-3:
            warnings.warn("High values detected! Activation mask not longer rescaled as default behaviour. Please set "
                          "rescale=True to map pixels in range [0, 1] or [0, 255] to the default stimulus scale.",
                          category=DeprecationWarning, stacklevel=2)
        return electrode_activation
