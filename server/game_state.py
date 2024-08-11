import copy
from sortedcontainers import SortedSet

# Global seq_to_idx dictionary
seq_to_idx = {
    "0_l": [0, 1, 3],
    "2_l": [2, 4, 6, 8],
    "5_l": [5, 7, 9, 11, 13],
    "10_l": [10, 12, 14, 16],
    "15_l": [15, 17, 18],
    "3_d": [3, 8, 13],
    "1_d": [1, 6, 11, 16],
    "0_d": [0, 4, 9, 14, 18],
    "2_d": [2, 7, 12, 17],
    "5_d": [5, 10, 15],
    "0_r": [0, 2, 5],
    "1_r": [1, 4, 7, 10],
    "3_r": [3, 6, 9, 12, 15],
    "8_r": [8, 11, 14, 17],
    "13_r": [13, 16, 18]
}

# Global idx_to_seq list
idx_to_seq = [
    ["0_l", "0_d", "0_r"],  # Index 0
    ["0_l", "1_d", "1_r"],  # Index 1
    ["0_r", "2_d", "2_l"],  # Index 2
    ["3_d", "0_l", "3_r"],  # Index 3
    ["2_l", "0_d", "1_r"],  # Index 4
    ["5_l", "0_r", "5_d"],  # Index 5
    ["2_l", "1_d", "3_r"],  # Index 6
    ["2_d", "1_r", "5_l"],  # Index 7
    ["2_l", "3_d", "8_r"],  # Index 8
    ["0_d", "5_l", "3_r"],  # Index 9
    ["10_l", "5_d", "1_r"], # Index 10
    ["5_l", "1_d", "8_r"],  # Index 11
    ["2_d", "10_l", "3_r"], # Index 12
    ["5_l", "3_d", "13_r"], # Index 13
    ["0_d", "10_l", "8_r"], # Index 14
    ["15_l", "5_d", "3_r"], # Index 15
    ["1_d", "10_l", "13_r"],# Index 16
    ["2_d", "15_l", "8_r"], # Index 17
    ["0_d", "15_l", "13_r"] # Index 18
]

DEFAULT_BOARD_SIZE = 19  # We now represent the board as a list of 19 elements

class GameState:
    def __init__(self, board=None, score=0, done=False, remaining_tiles=None):
        super(GameState, self).__init__()
        self._done = done
        self._score = score

        # Initialize the board as a list of 19 None elements if not provided
        if board is None:
            board = [None] * DEFAULT_BOARD_SIZE

        self._board = board

        # Initialize remaining tiles as a SortedSet if not provided
        if remaining_tiles is None:
            self._tiles = SortedSet(self.generate_tiles())
        else:
            self._tiles = SortedSet(remaining_tiles)

    def generate_tiles(self):
        i_values = [1, 5, 9]
        j_values = [2, 6, 7]
        k_values = [3, 4, 8]
        tiles = []
        for i in i_values:
            for j in j_values:
                for k in k_values:
                    tiles.append((i, j, k))  # Use tuples to store tiles
        return tiles

    def pop_random_tile(self, index):
        """Pop and return the tile at the given index from the sorted set of remaining tiles."""
        if not self._tiles or index < 0 or index >= len(self._tiles):
            return None
        return self._tiles.pop(index)  # Remove and return the tile at the given index

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
    def tiles(self):
        return self._tiles

    def get_legal_actions(self):
        # Legal actions are the indices on the board that are still None
        return [i for i, tile in enumerate(self._board) if tile is None]

    def apply_action(self, idx, tile):
        if self._board[idx] is not None:
            raise Exception("Illegal action: Tile placement on an already occupied spot.")

        # Place the tile on the board
        self._board[idx] = tile

        # Incrementally update the score
        self.update_score(idx, tile)

        # If no empty spots are left, the game is done
        if all(t is not None for t in self._board):
            self._done = True

    def update_score(self, idx, tile):
        """Update the score incrementally based on the tile placed at idx."""

        def calculate_score(indices, component_index):
            first_tile = self._board[indices[0]]
            if first_tile is None or first_tile[component_index] != tile[component_index]:
                return 0

            component_value = first_tile[component_index]
            for sub_idx in indices[1:]:
                current_tile = self._board[sub_idx]
                if current_tile is None or current_tile[component_index] != component_value:
                    return 0

            return component_value * len(indices)

        # Get the sequences (rows, columns, diagonals) that include the placed tile
        sequences = idx_to_seq[idx]

        # Update the score by calculating the contribution of the new tile in each sequence
        for seq in sequences:
            component_index = None
            if "_l" in seq:
                component_index = 1  # Left component
            elif "_d" in seq:
                component_index = 0  # Vertical component
            elif "_r" in seq:
                component_index = 2  # Right component

            # Add the score for this sequence
            self._score += calculate_score(seq_to_idx[seq], component_index)

    def generate_successor(self, idx, tile):
        successor = GameState(board=copy.deepcopy(self._board), score=self._score, done=self._done,
                              remaining_tiles=self._tiles.copy())  # Use copy() for SortedSet
        successor.apply_action(idx, tile)
        return successor

    def evaluate_game_state(self):
        total_score = 0

        def calculate_score(indices, component_index):
            first_tile = self._board[indices[0]]
            if first_tile is None:
                return 0

            component_value = first_tile[component_index]
            for idx in indices[1:]:
                tile = self._board[idx]
                if tile is None or tile[component_index] != component_value:
                    return 0

            return component_value * len(indices)

        # Calculate the score for each sequence
        for seq, indices in seq_to_idx.items():
            if "l" in seq:
                total_score += calculate_score(indices, 1)  # Left component
            elif "d" in seq:
                total_score += calculate_score(indices, 0)  # Vertical component
            elif "r" in seq:
                total_score += calculate_score(indices, 2)  # Right component

        self._score = total_score
        return total_score

    def is_game_over(self):
        return self._done

    def get_game_outcome(self):
        if self.is_game_over():
            return self.evaluate_game_state()
        return None  # Game is still ongoing
