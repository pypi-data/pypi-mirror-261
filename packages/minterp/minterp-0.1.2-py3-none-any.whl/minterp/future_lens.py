import torch

from minterp.model import MinterpModel
from minterp.state import StateConfig, StateManager
from minterp.context import Context


model = MinterpModel()


# Source context is all layers, all positions
source_context = Context("The quick brown fox jumps over the lazy dog", "gpt2", position="the lazy dog", layer="all")

# Create a state config for capturing each layer outputs on the first forward pass
state = StateManager(StateConfig(save_states="layer"))
model.run(source_context, state_manager=state)

# Target is a soft prompt
