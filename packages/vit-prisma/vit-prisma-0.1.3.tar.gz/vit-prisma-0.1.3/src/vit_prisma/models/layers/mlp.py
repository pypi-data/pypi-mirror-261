import torch.nn as nn
from vit_prisma.prisma_tools.hook_point import HookPoint
from vit_prisma.configs.HookedViTConfig import HookedViTConfig

from typing import Dict, Optional, Tuple, Union

from jaxtyping import Float, Int

import torch
import torch.nn.functional as F

import numpy as np

from vit_prisma.models.activation_fns import gelu_fast, gelu_new, solu

from vit_prisma.models.layers.layer_norm import LayerNorm, LayerNormPre

from fancy_einsum import einsum

class MLP(nn.Module):

    def __init__(self, cfg: Union[Dict, HookedViTConfig]):
        super().__init__()
        
        if not isinstance(cfg, HookedViTConfig):
            cfg = HookedViTConfig.from_dict(cfg)
        
        self.cfg = cfg

        self.W_in = nn.Parameter(
            torch.empty(self.cfg.d_model, self.cfg.d_mlp, dtype=self.cfg.dtype)
        )
        self.b_in = nn.Parameter(
            torch.empty(self.cfg.d_mlp, dtype=self.cfg.dtype)
        )
        self.W_out = nn.Parameter(
            torch.empty(self.cfg.d_mlp, self.cfg.d_model, dtype=self.cfg.dtype)
        )
        self.b_out = nn.Parameter(
            torch.empty(self.cfg.d_model, dtype=self.cfg.dtype)
        )

        self.hook_pre = HookPoint()
        self.hook_post = HookPoint()

        if self.cfg.activation_name == "relu":
                self.act_fn = F.relu
        elif self.cfg.activation_name == "gelu":
            self.act_fn = F.gelu
        elif self.cfg.activation_name == "silu":
            self.act_fn = F.silu
        elif self.cfg.activation_name == "gelu_new":
            self.act_fn = gelu_new
        elif self.cfg.activation_name == "gelu_fast":
            self.act_fn = gelu_fast
        elif self.cfg.activation_name == "solu_ln": # why does only solu have a layernorm? 
            self.act_fn = solu
            # Hook taken between activation and layer norm
            self.hook_mid = HookPoint()  # [batch, pos, d_mlp]
            if self.cfg.normalization_type == "LN":
                self.ln = LayerNorm(self.cfg, self.cfg.d_mlp)
            else:
                self.ln = LayerNormPre(self.cfg)

        else:
            raise ValueError(f"Invalid activation function name: {self.cfg.activation_name}")
    
    def forward(self, x: Float[torch.Tensor, "batch pos d_model"]
    ) -> Float[torch.Tensor, "batch pos d_model"]:
        
        pre_act = self.hook_pre(
              einsum("batch pos d_model, d_model d_mlp -> batch pos d_mlp", x, self.W_in)
            + self.b_in
        )
        if not self.cfg.activation_name.endswith("_ln"):
              post_act = self.hook_post(self.act_fn(pre_act))
        else:
              mid_act = self.hook_mid(self.act_fn(pre_act))
              post_act = self.hook_post(self.ln(mid_act))
        return (
              einsum("batch pos d_mlp, d_mlp d_model -> batch pos d_model", post_act, self.W_out) 
              + self.b_out
        )
          
