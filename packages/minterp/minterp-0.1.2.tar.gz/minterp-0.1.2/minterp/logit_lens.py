import torch

from minterp.model import MinterpModel
from minterp.state import StateConfig, StateManager
from minterp.context import Context
from minterp.vis import create_annotated_heatmap


class LogitLens:
    def __init__(self, source_context):
        self.source_context = source_context
        self.model = MinterpModel(self.source_context.model_name)
        self.target_context = self.source_context.clone_with_overrides(layer=-1)

    def source(self):
        # Create a state config for capturing on the first forward pass
        self.state = StateManager(StateConfig(save_states=["layer"]))
        self.model.run(self.source_context, state_manager=self.state)

    def target(self):
        # Create a state config for manipulating the states on the second forward pass
        for i in range(self.model.n_layers):
            yield f"Running layer {i}..."
            self.state.update_config(StateConfig(load_states=f"layer_{i}", save_states="lm_head", concate_outputs="lm_head"))
            self.model.run(self.target_context, state_manager=self.state)

    def vis(self):
        lm_head = self.state.pop_state('lm_head')
        # The state now has dims (batch, tokens, logits)
        # Where the batches are the layers.
        # Get the probs for the top prediction for each token in the substring
        probs, indices = torch.topk(lm_head, k=1, dim=-1)
        probs = probs.squeeze(-1).numpy()
        indices = indices.squeeze(-1).numpy()

        # Make a list of lists of words
        words = [[self.model.tokenizer.decode([i]) for i in tokens] for tokens in indices]

        prompt_tokens = self.model.tokenizer.encode(self.source_context.prompt)
        x_ticks = [self.model.tokenizer.decode([i]) for i in prompt_tokens[self.model.positions_to_process]]
        y_ticks = [f"layer_{i}" for i in list(range(self.model.n_layers))]

        # create a heatmap with the top logits and predicted tokens
        self.fig = create_annotated_heatmap(probs, words, x_ticks, y_ticks, title='Top predicted token and its logit')
        return self.fig

    def run(self):
        self.source()
        list(self.target())
        return self


if __name__ == "__main__":
    # Source context is all layers, all positions
    prompt = "The quick brown fox jumps over the lazy dog."
    model = "gpt2"
    source_context = Context(prompt, model, position="the lazy dog", layer="all")
    ll = LogitLens(source_context)
    for status in ll.run().target():
        print(status)
    fig = ll.vis()
    fig.show()
