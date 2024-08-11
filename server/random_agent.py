import numpy as np
from game import Agent, PlacementAction, Action

class RandomAgent(Agent):
    def get_action(self, game_state, tile):
        # Get all legal actions (available positions) on the board
        empty_tiles = game_state.get_legal_actions(0)

        # If there are no legal actions, return STOP
        if not empty_tiles:
            return Action.STOP

        # Randomly choose an available position on the board
        placement_index = np.random.choice(len(empty_tiles))
        index = empty_tiles[placement_index]

        # Return the action with the chosen index
        return PlacementAction(index=index)
