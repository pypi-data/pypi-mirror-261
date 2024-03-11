import torch

from minterp.model import MinterpModel
from minterp.state import StateConfig, StateManager
from minterp.context import Context
from minterp.vis import create_annotated_heatmap


model = MinterpModel()

source_prompt = "The quick brown fox jumps over the lazy dog"
identity_prompt = "bat is bat; 135 is 135; hello is hello; black is black; shoe is shoe; x is"
source_context = Context(source_prompt, "gpt2", position="all", layer="all")

# Create a state config for capturing on the first forward pass
state = StateManager(StateConfig(save_states=["layer", "lm_head"]))
model.run(source_context, state_manager=state)

# Get the lm_head outputs
lm_head_original = state.pop_state("lm_head")

# For each layer and position, run a forward pass with the token identity prompt
source_tokens = model.tokenizer.encode(source_prompt)
for i in range(model.n_layers):
    config = StateConfig(load_states=f"layer_{i}", save_states="lm_head", concate_outputs="lm_head")
    for j in range(len(source_tokens)):
        target_context = Context(identity_prompt, "gpt2", position="all", layer=i)
        # Set up the position map for each token
        config.position_maps[f"layer_{i}"] = (j, -1)
        state.update_config(config)
        model.run(target_context, state_manager=state)


lm_head = state.get_state('lm_head').detach()
# The outputs are all at the last position of the lm_head, which has dims
# (n_layers * len(source_tokens), len(target_tokens), vocab_size)
# First we get the probs and indices for the final token in each pseudobatch
probs, indices = torch.topk(lm_head[:, -1], k=1, dim=-1)

# Then we reshape the probs and indices to be (n_layers, len(source_tokens), vocab_size)
probs = probs.view(model.n_layers, len(source_tokens), -1).squeeze(-1)
indices = indices.view(model.n_layers, len(source_tokens), -1).squeeze(-1)

# Get the probs and indicies from the original lm_head and concat them
probs_original, indices_original = torch.topk(lm_head_original, k=1, dim=-1)
probs_original = probs_original.squeeze(-1)
indices_original = indices_original.squeeze(-1)

probs = torch.cat([probs, probs_original], dim=0).numpy()
indices = torch.cat([indices, indices_original], dim=0).numpy()

# Make a list of lists of words
words = [[model.tokenizer.decode([i]) for i in tokens] for tokens in indices]

x_ticks = [model.tokenizer.decode([i]) for i in source_tokens]
y_ticks = [f"layer_{i}" for i in list(range(model.n_layers + 1))]

# create a heatmap with the top logits and predicted tokens
fig = create_annotated_heatmap(probs, words, x_ticks, y_ticks, title='Top predicted token and its logit')
fig.show()
