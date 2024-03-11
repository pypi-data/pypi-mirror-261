from dataclasses import dataclass, field
from typing import Sequence, Union
import copy

import torch


@dataclass
class Context:
    # Prompt can be a string or a soft prompt
    prompt: Union[str, torch.Tensor]
    model_name: str
    # Position can be a single integer, a sequence of integers or a slice expression
    position: Union[int, Sequence[int], str] = field(default_factory=lambda: [-1])
    # Layer can be a single integer, a sequence of integers or a slice expression
    layer: Union[int, Sequence[int], str] = "all"
    device: str = "cuda" if torch.cuda.is_available() else "cpu"

    def __post_init__(self):
        # Convert single integers to sequences for uniform processing
        if isinstance(self.position, int):
            self.position = [self.position]
        if isinstance(self.layer, int):
            self.layer = [self.layer]

    def clone_with_overrides(self, **kwargs):
        """
        Create a copy of the context with overrides for specific fields.

        Usage:
            new_context = old_context.clone_with_overrides(prompt="New prompt", layer=5)
        """
        new_instance = copy.deepcopy(self)  # Use deepcopy if you need to copy mutable objects within the class
        for attribute, value in kwargs.items():
            setattr(new_instance, attribute, value)
        return new_instance
