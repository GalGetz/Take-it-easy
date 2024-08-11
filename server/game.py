import abc
from collections import namedtuple
from enum import Enum
import numpy as np
import time


class Action(Enum):
  PLACE_TILE = 1
  STOP = 2


PlacementAction = namedtuple('PlacementAction', ['row', 'column', 'tile'])


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
  def get_action(self, game_state, available_tiles):
    if not available_tiles:
      return Action.STOP
    # Randomly choose a tile for the main agent to place
    tile = available_tiles.pop(np.random.choice(len(available_tiles)))
    return tile


class Game(object):
  def __init__(self, agent, opponent_agent, sleep_between_actions=False):
    super(Game, self).__init__()
    self.sleep_between_actions = sleep_between_actions
    self.agent = agent
    self.opponent_agent = opponent_agent
    self._state = None
    self._should_quit = False
    self.tiles = self.generate_tiles()
    np.random.shuffle(self.tiles)  # Shuffle tiles to ensure randomness

  def generate_tiles(self):
    i_values = [1, 5, 9]
    j_values = [2, 6, 7]
    k_values = [3, 4, 8]
    tiles = []
    for i in i_values:
      for j in j_values:
        for k in k_values:
          tiles.append([i, j, k])
    return tiles

  def run(self, initial_state):
    self._should_quit = False
    self._state = initial_state
    return self._game_loop()

  def quit(self):
    self._should_quit = True
    self.agent.stop_running()
    self.opponent_agent.stop_running()

  def _game_loop(self):
    while not self._state.done and not self._should_quit and self.tiles:
      if self.sleep_between_actions:
        time.sleep(1)

      # The opponent agent selects the tile
      tile = self.opponent_agent.get_action(self._state, self.tiles)
      if tile == Action.STOP or not tile:
        return

      # The main agent decides where to place the selected tile
      action = self.agent.get_action(self._state, tile)
      if action == Action.STOP:
        return
      self._state.apply_action((action.row, action.column), tile)

    return self._state.score
