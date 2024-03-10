import torch
import torch.nn as nn

import einops

from vit_prisma.configs.HookedViTConfig import HookedViTConfig

from typing import Dict, Optional, Tuple, Union

from jaxtyping import Float, Int

class PosEmbedding(nn.Module):

    def __init__(self, cfg: Union[Dict, HookedViTConfig]):

        super().__init__()

        if isinstance(cfg, Dict):
            cfg = HookedViTConfig.from_dict(cfg)
        self.cfg = cfg

        num_patches = (self.cfg.image_size // self.cfg.patch_size)**2
        if self.cfg.is_video_transformer:
            num_patches = num_patches*(self.cfg.video_num_frames//self.cfg.video_tubelet_depth)
            
        token_length = num_patches + 1 if self.cfg.classification_type == 'cls' else num_patches

        self.W_pos = nn.Parameter(
            torch.empty(token_length, self.cfg.d_model, dtype=self.cfg.dtype)
        )
    
    def forward(
            self,
            tokens: Int[torch.Tensor, "batch pos"],
    ):
        pos_embed = self.W_pos
        batch_pos_embed = einops.repeat(pos_embed, "pos d_model -> batch pos d_model", batch=tokens.size(0))
        return batch_pos_embed

