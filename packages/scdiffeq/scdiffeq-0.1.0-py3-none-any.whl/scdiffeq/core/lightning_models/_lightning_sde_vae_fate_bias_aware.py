
# -- import packages: ----------------------------------------------------------
from neural_diffeqs import NeuralSDE
import torch


# -- import local dependencies: ------------------------------------------------
from . import base, mix_ins


from typing import Optional, Union, List

from ... import __version__


# -- lightning model: ----------------------------------------------------------
class LightningSDE_VAE_FateBiasAware(
    mix_ins.VAEMixIn,
    mix_ins.FateBiasVAEMixIn,
    mix_ins.PotentialMixIn,
    mix_ins.PreTrainMixIn,
    base.BaseLightningDiffEq,
):
    def __init__(
        self,
        data_dim,
        latent_dim: int = 50,
        name: Optional[str] = None,
        train_lr=1e-5,
        pretrain_lr=1e-3,
        pretrain_epochs=100,
        pretrain_optimizer=torch.optim.Adam,
        train_optimizer=torch.optim.RMSprop,
        pretrain_scheduler=torch.optim.lr_scheduler.StepLR,
        train_scheduler=torch.optim.lr_scheduler.StepLR,
        pretrain_step_size=200,
        train_step_size=10,
        dt=0.1,
        adjoint=False,
        backend = "auto",
        
        # -- sde params: -------------------------------------------------------
        mu_hidden: Union[List[int], int] = [400, 400, 400],
        sigma_hidden: Union[List[int], int] = [400, 400, 400],
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
        
        # -- encoder parameters: -----------------------------------------------
        encoder_n_hidden: int = 4,
        encoder_power: float = 2,
        encoder_activation: Union[str, List[str]] = 'LeakyReLU',
        encoder_dropout: Union[float, List[float]] = 0.2,
        encoder_bias: bool = True,
        encoder_output_bias: bool = True,
        
        # -- decoder parameters: -----------------------------------------------
        decoder_n_hidden: int = 4,
        decoder_power: float = 2,
        decoder_activation: Union[str, List[str]] = 'LeakyReLU',
        decoder_dropout: Union[float, List[float]] = 0.2,
        decoder_bias: bool = True,
        decoder_output_bias: bool = True,

        # -- fate bias parameters: ---------------------------------------------
        t0_idx = None,
        kNN_Graph=None,
        fate_bias_csv_path=None,
        fate_bias_multiplier = 1,
        
        PCA = None,
        
        loading_existing: bool = False,
        version = __version__,
        
        *args,
        **kwargs,
    ):
        super().__init__()

        name = self._configure_name(name, loading_existing=loading_existing)
        
        self.save_hyperparameters(ignore=['kNN_Graph'])
                        
        # -- torch modules: ----------------------------------------------------
        self._configure_torch_modules(func=NeuralSDE, kwargs=locals())
        self._configure_lightning_model(kwargs = locals())
        
        self._configure_fate(
            graph=kNN_Graph,
            csv_path = fate_bias_csv_path,
            t0_idx = t0_idx,
            fate_bias_multiplier = fate_bias_multiplier,
            PCA = PCA,
        )

    def __repr__(self):
        return "LightningSDE-VAE-FateBiasAware"
