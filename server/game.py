import abc
from collections import namedtuple
from enum import Enum
import numpy as np


class Action(Enum):
    PLACE_TILE = 1
    STOP = 2


# Updated PlacementAction to only include the index
PlacementAction = namedtuple('PlacementAction', ['index'])


class Agent(object):
    def __init__(self):
        super(Agent, self).__init__()

    @abc.abstractmethod
    def get_action(self, game_state):
        """This method decides where to place the tile."""
        return

    def stop_running(self):
        pass


class RandomOpponentAgent(Agent):
    def __init__(self):
        super().__init__()
        self.rng = np.random.default_rng()  # Create a random number generator

    def get_action(self, game_state):
        if not game_state.tiles:
            return Action.STOP

        # Randomly choose an index from the sorted set using the random number generator
        index = self.rng.choice(len(game_state.tiles))

        # Pop the tile from the sorted set at the chosen index
        tile = game_state.pop_random_tile(index)
        return tile


class Game:
    def __init__(self, agent, opponent_agent):
        super(Game, self).__init__()
        self.agent = agent
        self.opponent_agent = opponent_agent
        self._state = None
        self._should_quit = False

    def initialize(self, initial_state):
        """Initialize the game with the initial state."""
        self._state = initial_state
        self._should_quit = False

    def current_tile(self):
        """Run the opponent's step, returning the tile drawn by the opponent."""
        if self._state.done or self._should_quit or not self._state.tiles:
            return None

        # The opponent agent selects the tile
        tile = self.opponent_agent.get_action(self._state)
        if tile == Action.STOP or not tile:
            return None

        # Set the current tile in the game state
        self._state.set_current_tile(tile)
        return tile

    def agent_location(self):
        """Run the agent's step, returning the location where the tile is placed."""
        if self._state.done or self._should_quit:
            return None

        # The main agent decides where to place the selected tile
        action = self.agent.get_action(self._state)
        if action == Action.STOP:
            return None

        # Apply the chosen action to the game state
        self._state.apply_action(action)

        return action.index

    def quit(self):
        self._should_quit = True
        self.agent.stop_running()
        self.opponent_agent.stop_running()
