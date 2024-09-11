from game import Agent
import game_state
import numpy as np
from expectimax_agent import Expectimax



class Reflex(Agent):
    def __init__(self):
        super(Reflex, self).__init__()

        self.expectimaxAgent = Expectimax(max_depth=0, max_actions=27, evaluation_function=self.reflex_evaluation_function)

    def get_action(self, game_state):
        """
        Returns the current action
        """
        return self.expectimaxAgent.get_action(game_state)
        

    def reflex_evaluation_function(self, state):
        """Default evaluation function that returns the current score of the game state."""

        partial_sequences = 0
        for seq, index in game_state.seq_to_idx.items():
            component_index = None
            if "_l" in seq:
                component_index = 2  # Right component
            elif "_d" in seq:
                component_index = 0  # Vertical component
            elif "_r" in seq:
                component_index = 1  # Left component
            mask = ~np.isnan(state.board[index][:,0])
            filtered_list = state.board[index][mask][:, component_index].astype(int)
            sum_values = np.sum(filtered_list)
            unique_values = np.unique(filtered_list)
            different_values = unique_values.size

            if different_values == 1:
                partial_sequences += unique_values[0]

        return partial_sequences
