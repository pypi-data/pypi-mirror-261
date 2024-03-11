from typing import Union

import torch
from nnsight import LanguageModel

from minterp.context import Context
from minterp.state import StateManager


class MinterpModel(LanguageModel):
    MASK_WORD = " _"

    def __init__(self, model_name: str = "gpt2", device_map: str = "cpu", *args, **kwargs) -> None:
        super().__init__(model_name, device_map=device_map, *args, **kwargs)
        self.model_name = model_name
        self.device_map = device_map

    @property
    def model_specifics(self):
        """
        Get the model specific attributes.
        The following works for gpt2, llama2 and mistral models.
        """
        if "gpt" in self.model_name:
            return "transformer", "h", "wte"
        if "mamba" in self.model_name:
            return "backbone", "layers", "embed_tokens"
        return "model", "layers", "embed_tokens"

    @property
    def layers(self):
        return getattr(getattr(self, self.model_specifics[0]), self.model_specifics[1])

    @property
    def embed(self):
        return getattr(getattr(self, self.model_specifics[0]), self.model_specifics[2])

    @property
    def n_layers(self):
        return len(getattr(getattr(self, self.model_specifics[0]), self.model_specifics[1]))

    def run(self, context: Context, state_manager: StateManager):
        layers_to_process = self._resolve_layers(context.layer)
        positions_to_process = self._resolve_positions(context.prompt, context.position)
        self.layers_to_process, self.positions_to_process = layers_to_process, positions_to_process

        with self.trace(self.prompt_text(context.prompt)):
            # Can save the initial embeddings out
            if "embed" in state_manager.config.save_states:
                state_manager.add_state("embed", self.embed.output.save())
            # Support soft prompts as prompts.
            if isinstance(context.prompt, torch.Tensor):
                self.embed.output = context.prompt
            # If you have something else loaded in by the state manager, it will override the soft prompt
            if "embed" in state_manager.config.load_states:
                self.embed.output = state_manager.get_state("embed")
            # We can save many states at once
            if "layer" in state_manager.config.save_states:
                for layer in layers_to_process:
                    state_manager.add_state(f"layer_{layer}", self.layers[layer].output[0][:, positions_to_process, :].save())
            # Loading state is handled in the state manager
            for source_layer in [name for name in state_manager.config.load_states if "layer" in name]:
                for layer in layers_to_process:
                    source_state = state_manager.get_state(source_layer)
                    slice_size = positions_to_process.stop - positions_to_process.start
                    if source_layer in state_manager.config.position_maps:
                        source_position, target_position = state_manager.config.position_maps[source_layer]
                    elif source_state.size(1) == slice_size:
                        source_position, target_position = slice(0, slice_size), positions_to_process
                    else:
                        source_position, target_position = positions_to_process, positions_to_process
                    self.layers[layer].output[0][:, target_position, :] = source_state[:, source_position, :]
            if "lm_head" in state_manager.config.save_states:
                state_manager.add_state("lm_head", self.lm_head.output[:, positions_to_process, :].save())

    def prompt_text(self, prompt: Union[str, torch.Tensor]):
        """
        If its a soft prompt, create a mask long enough
        """
        if isinstance(prompt, str):
            return prompt
        return "".join([self.MASK_WORD] * prompt.size(0))

    def _resolve_layers(self, layer_spec):
        if isinstance(layer_spec, str):
            return parse_dynamic_slice(layer_spec, self.n_layers)

        if isinstance(layer_spec, (int, list)):
            return [layer_spec] if isinstance(layer_spec, int) else layer_spec

    def _resolve_positions(self, prompt, position_spec):
        if isinstance(prompt, torch.Tensor):
            return slice(0, prompt.size(0))
        if isinstance(position_spec, str):
            prompt_tokens = self.tokenizer.encode(prompt)
            if position_spec == "all":
                return slice(0, len(prompt_tokens))

            return self._find_tokens(prompt_tokens, position_spec)

        if isinstance(position_spec, int):
            return slice(position_spec, position_spec + 1)
        if isinstance(position_spec, list):
            return slice(position_spec[0], position_spec[-1] + 1)

    def _find_tokens(self, prompt, position_spec):
        """
        Find the indices of a phrase in a prompt.
        """
        position_tokens = self.tokenizer.encode(position_spec)
        if position_tokens[0] not in prompt:
            position_tokens = self.tokenizer.encode(" " + position_spec)
            if position_tokens[0] not in prompt:
                raise ValueError(f"Phrase '{position_spec}' not found in prompt.")

        return find_window_index(prompt, position_tokens)


def find_window_index(large_list, window):
    window_length = len(window)
    # Loop through the larger list
    for i in range(len(large_list) - window_length + 1):
        # Compare slices of the larger list with the target window
        if large_list[i:i + window_length] == window:
            return slice(i, i + window_length)
    raise ValueError("Phrase not found in prompt.")


def parse_dynamic_slice(slice_str, n):
    """
    Parses a string representing a slice with dynamic expressions involving 'n' and
    returns a list of indices within the range of 0 to n.
    """
    # Special handling for 'all' or ':' indicating full range
    if not slice_str or slice_str in ["all", ":"]:
        return list(range(n))

    parts = slice_str.split(':')
    if len(parts) == 3:
        start_part, stop_part, step_part = parts
    elif len(parts) == 2:
        start_part, stop_part = parts
        step_part = "1"
    else:
        raise ValueError("Invalid slice specification")

    # Secure environment for eval
    safe_dict = {'n': n}

    # Calculate start, stop, and step using eval in a controlled environment
    start = eval(start_part or "None", {"__builtins__": {}}, safe_dict) if start_part else None
    stop = eval(stop_part or "None", {"__builtins__": {}}, safe_dict) if stop_part else None
    step = eval(step_part or "None", {"__builtins__": {}}, safe_dict) if step_part else None

    return list(range(n))[slice(start, stop, step)]
