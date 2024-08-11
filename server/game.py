import abc
from collections import namedtuple
from enum import Enum
import numpy as np
import time

class Action(Enum):
    PLACE_TILE = 1
    STOP = 2

# Updated PlacementAction to only include the index
PlacementAction = namedtuple('PlacementAction', ['index'])

class Agent(object):
    def __init__(self):
        super(Agent, self).__init__()

    @abc.abstractmethod
    def get_action(self, game_state, tile):
        """This method decides where to place the tile."""
        return

    def stop_running(self):
        pass

class RandomOpponentAgent(Agent):
    def get_action(self, game_state, tile=None):
        if not game_state.tiles:
            return Action.STOP
        # Randomly choose an index from the sorted set
        index = np.random.choice(len(game_state.tiles))
        # Pop the tile from the sorted set at the chosen index
        tile = game_state.pop_random_tile(index)
        return tile

class Game(object):
    def __init__(self, agent, opponent_agent, sleep_between_actions=False):
        super(Game, self).__init__()
        self.sleep_between_actions = sleep_between_actions
        self.agent = agent
        self.opponent_agent = opponent_agent
        self._state = None
        self._should_quit = False

    def run(self, initial_state):
        self._should_quit = False
        self._state = initial_state
        return self._game_loop()

    def quit(self):
        self._should_quit = True
        self.agent.stop_running()
        self.opponent_agent.stop_running()

    def _game_loop(self):
        while not self._state.done and not self._should_quit and self._state.tiles:
            if self.sleep_between_actions:
                time.sleep(1)

            # The opponent agent selects the tile
            tile = self.opponent_agent.get_action(self._state)
            if tile == Action.STOP or not tile:
                return

            # The main agent decides where to place the selected tile
            action = self.agent.get_action(self._state, tile)
            if action == Action.STOP:
                return
            self._state.apply_action(action.index, tile)

        return self._state.score
