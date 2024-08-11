import copy
import numpy as np

DEFAULT_BOARD_SIZE = (9, 5)  # Adjusted to fit the provided 9x5 board


class GameState(object):
  def __init__(self, rows=9, columns=5, board_layout=None, board=None, score=0, done=False, remaining_tiles=None):
    super(GameState, self).__init__()
    self._done = done
    self._score = score

    # Default board layout if none is provided
    if board_layout is None:
      board_layout = [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0]
      ]

    self._board_layout = np.array(board_layout)

    if board is None:
      # Initialize the board with None, except for positions where board_layout is 1
      board = np.full((rows, columns), None, dtype=object)
      for r in range(rows):
        for c in range(columns):
          if board_layout[r][c] == 1:
            board[r][c] = [None, None, None]  # Placeholder for [vertical, left, right]

    self._board = board
    self._num_of_rows, self._num_of_columns = rows, columns
    self._remaining_tiles = remaining_tiles if remaining_tiles is not None else []

  @property
  def done(self):
    return self._done

  @property
  def score(self):
    return self._score

  @property
  def board(self):
    return self._board

  @property
  def remaining_tiles(self):
    return self._remaining_tiles

  def get_legal_actions(self):
    # Legal actions are all empty tiles in valid positions according to the layout
    empty_tiles = self.get_empty_tiles()
    legal_actions = []
    for i in range(empty_tiles[0].size):
      row, col = empty_tiles[0][i], empty_tiles[1][i]
      legal_actions.append((row, col))
    return legal_actions

  def get_empty_tiles(self):
    # This function returns the positions of all empty tiles that are still [None, None, None].
    return np.where(self._board == [None, None, None])

  def apply_action(self, action, tile):
    row, col = action
    if self._board[row][col] != [None, None, None]:
      raise Exception("Illegal action: Tile placement on an already occupied or illegal spot.")
    self._board[row][col] = tile
    if self.get_empty_tiles()[0].size == 0:  # If no empty spots left, game is done
      self._done = True

  def generate_successor(self, action, tile):
    successor = GameState(rows=self._num_of_rows, columns=self._num_of_columns, board_layout=self._board_layout,
                          board=copy.deepcopy(self._board), score=self._score, done=self._done,
                          remaining_tiles=copy.deepcopy(self._remaining_tiles))
    successor.apply_action(action, tile)
    return successor

  def evaluate_game_state(self):
    total_score = 0

    # Corrected Column indices for vertical component scoring
    column_indices = [
      [(2, 0), (4, 0), (6, 0)],  # Column 1
      [(1, 1), (3, 1), (5, 1), (7, 1)],  # Column 2
      [(0, 2), (2, 2), (4, 2), (6, 2), (8, 2)],  # Column 3
      [(1, 3), (3, 3), (5, 3), (7, 3)],  # Column 4
      [(2, 4), (4, 4), (6, 4)]  # Column 5
    ]

    # Corrected Left diagonal indices for left component scoring
    left_diagonal_indices = [
      [(0, 2), (1, 3), (2, 4)],  # Diagonal 1
      [(1, 1), (2, 2), (3, 3), (4, 4)],  # Diagonal 2
      [(2, 0), (3, 1), (4, 2), (5, 3), (6, 4)],  # Diagonal 3
      [(4, 0), (5, 1), (6, 2), (7, 3)],  # Diagonal 4
      [(6, 0), (7, 1), (8, 2)]  # Diagonal 5
    ]

    # Corrected Right diagonal indices for right component scoring
    right_diagonal_indices = [
      [(0, 2), (1, 1), (2, 0)],  # Diagonal 1
      [(1, 3), (2, 2), (3, 1), (4, 0)],  # Diagonal 2
      [(2, 4), (3, 3), (4, 2), (5, 1), (6, 0)],  # Diagonal 3
      [(4, 4), (5, 3), (6, 2), (7, 1)],  # Diagonal 4
      [(6, 4), (7, 3), (8, 2)]  # Diagonal 5
    ]

    def calculate_score(indices, component_index):
      first_tile = self._board[indices[0][0]][indices[0][1]]
      if first_tile is None or first_tile[component_index] is None:
        return 0

      component_value = first_tile[component_index]
      for (row, col) in indices[1:]:
        tile = self._board[row][col]
        if tile is None or tile[component_index] != component_value:
          return 0

      return component_value * len(indices)

    # Calculate column scores
    for col_set in column_indices:
      total_score += calculate_score(col_set, 0)  # Vertical component

    # Calculate left diagonal scores
    for diag_set in left_diagonal_indices:
      total_score += calculate_score(diag_set, 1)  # Left component

    # Calculate right diagonal scores
    for diag_set in right_diagonal_indices:
      total_score += calculate_score(diag_set, 2)  # Right component

    self._score = total_score
    return total_score

  def is_game_over(self):
    return self._done

  def get_game_outcome(self):
    if self.is_game_over():
      return self.evaluate_game_state()
    return None  # Game is still ongoing
