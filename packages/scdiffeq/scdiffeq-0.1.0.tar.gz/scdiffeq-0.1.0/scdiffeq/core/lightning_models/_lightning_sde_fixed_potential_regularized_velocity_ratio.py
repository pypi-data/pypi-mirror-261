
from neural_diffeqs import PotentialSDE
import torch


from . import base, mix_ins
from typing import Dict, List, Optional, Union

from ... import __version__


# -- lightning model: -----------------------------------
class LightningSDE_FixedPotential_RegularizedVelocityRatio(
    mix_ins.PotentialMixIn,
#     mix_ins.BaseForwardMixIn,
    mix_ins.RegularizedVelocityRatioMixIn,
    base.BaseLightningDiffEq,
):
    def __init__(
        self,
        latent_dim: int = 50,
        velocity_ratio_params: Dict[str,Union[float,bool]] = {
            "target": 1,
            "enforce": 0, # zero to disable
            "method": "square", # abs -> calls torch.abs or torch.square
        },
        name: Optional[str] = None,
        mu_hidden: Union[List[int], int] = [2000, 2000],
        sigma_hidden: Union[List[int], int] = [800, 800],
        mu_activation: Union[str, List[str]] = 'LeakyReLU',
        sigma_activation: Union[str, List[str]] = 'LeakyReLU',
        mu_dropout: Union[float, List[float]] = 0.1,
        sigma_dropout: Union[float, List[float]] = 0.1,
        mu_bias: bool = True,
        sigma_bias: List[bool] = True,
        mu_output_bias: bool = True,
        sigma_output_bias: bool = True,
        mu_n_augment: int = 0,
        sigma_n_augment: int = 0,
        sde_type='ito',
        noise_type='general',
        brownian_dim=1,
        coef_drift: float = 1.0,
        coef_diffusion: float = 1.0,
        
        train_lr: float = 1e-4,
        train_optimizer=torch.optim.RMSprop,
        train_scheduler=torch.optim.lr_scheduler.StepLR,
        train_step_size: int = 10,
        dt: float = 0.1,
        adjoint = False,
        backend = "auto",
        loading_existing: bool = False,
        
        version = __version__,
        
        *args,
        **kwargs,
    ):
        super().__init__()
        
        name = self._configure_name(name, loading_existing = loading_existing)
        
        self.save_hyperparameters()
        
        # -- torch modules: ----------------------------------------------------
        self._configure_torch_modules(func=PotentialSDE, kwargs=locals())
        self._configure_lightning_model(kwargs = locals())

    def __repr__(self):
        return "LightningSDE-FixedPotential-RegularizedVelocityRatio"
