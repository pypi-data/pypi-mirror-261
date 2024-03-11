from typing import Optional
from nnsight.models.LanguageModel import LanguageModelProxy

import torch


class StateMap:
    def __init__(self, map_fn, retain_original=True):
        self.map_fn = map_fn
        self.retain_original = retain_original

    def apply(self, state_name, state_tensor):
        mapped_state_name = f"mapped_{state_name}"
        mapped_state_tensor = self.map_fn(state_tensor)
        if self.retain_original:
            return {state_name: state_tensor, mapped_state_name: mapped_state_tensor}
        else:
            return {mapped_state_name: mapped_state_tensor}


class StateConfig:
    def __init__(self, save_states=None, load_states=None, state_maps=None, position_maps=None, concate_outputs=None):
        """
        save_states: A list of state keys to save.
        load_states: A list of state keys to load into the model.
        state_maps: A dictionary where keys are metric names and values are tuples specifying
                         the state transformation function and the arguments needed apart from the state itself.
        position_maps: A dictionary where keys are state names and values are tuples specifying
                            the source and target positions for the state.
        concate_outputs: A list of state keys to concatenate along the batch dimension.
        """
        if isinstance(save_states, str):
            save_states = [save_states]
        self.save_states = save_states or []
        if isinstance(load_states, str):
            load_states = [load_states]
        self.load_states = load_states or []
        if isinstance(concate_outputs, str):
            concate_outputs = [concate_outputs]
        self.concate_outputs = concate_outputs or []

        self.state_maps = state_maps or {}
        self.position_maps = position_maps or {}

    def __repr__(self):
        return (
            f"StateConfig(save_states={self.save_states}, "
            f"load_states={self.load_states}, "
            f"state_maps={self.state_maps.keys()}, "
            f"position_maps={self.position_maps.keys()}"
        )


class StateManager:
    def __init__(self, config: StateConfig):
        self.config = config
        self.states = {}

    def __repr__(self):
        sizes = {k: v.shape for k, v in self.states.items()}
        return f"StateManager(config={self.config}, states={sizes})"

    def update_config(self, config: StateConfig):
        self.config = config

    def add_state(self, name: str, state_tensor: torch.Tensor):
        if name in self.config.state_maps:
            states = self.config.state_maps[name].apply(name, state_tensor)
            for name, state in states.items():
                self._save_state(name, state)
        else:
            self._save_state(name, state_tensor)

    def _save_state(self, name: str, state_tensor: torch.Tensor):
        if name in self.states and name in self.config.concate_outputs:
            self.states[name] = torch.cat([self.states[name], state_tensor], dim=0).detach()
        else:
            self.states[name] = state_tensor.detach()
        if isinstance(self.states[name], LanguageModelProxy):
            self.states[name] = self.states[name].save()

    def get_state(self, name: str) -> torch.Tensor:
        return self.states.get(name)

    def pop_state(self, name: str) -> torch.Tensor:
        return self.states.pop(name)

    def load_state(self, name: str, target_state: Optional[torch.Tensor] = None) -> torch.Tensor:
        """
        When getting the state, if there is a position mapping for that state,
        we will need the target tensor to get the dims.
        """
        if name in self.config.position_maps:
            return self.get_state_with_mapping(name, target_state)
        return self.states.get(name)

    def get_state_with_mapping(self, name: str, target_state: torch.Tensor) -> torch.Tensor:
        """Applies mapping to a state before returning it"""
        if target_state is None:
            raise ValueError("Target state is required for getting state with position mapping.")
        source_state = self.states.get(name)
        source_position, target_position = self.config.position_maps[name]
        target_state[:, target_position, :] = source_state[:, source_position, :]
        return target_state

    def clear(self):
        """
        Clear all states (and optionally metrics).
        """
        self.states.clear()
