import time
from game import Agent, Action, PlacementAction
import game_state
import numpy as np

from functools import lru_cache


class Expectimax(Agent):
    def __init__(self, weights=None, max_depth=5, max_actions=27, evaluation_function=None):
        super(Expectimax, self).__init__()
        self.weights = weights if weights is not None else [10, 2, 10, 1, 1]  # Default weights
        self.max_depth = max_depth
        self.max_actions = max_actions
        self.evaluation_function = evaluation_function if evaluation_function else self.default_evaluation_function

    def get_action(self, game_state):
        """
        Returns the expectimax action using dynamic depth adjustment and dynamic number of opponent actions.

        The opponent is modeled as choosing uniformly at random from their legal moves.
        """

        def expectimax(state, depth, agent_index, max_depth, max_actions):
            if state.done or depth == max_depth:
                return self.evaluation_function(state)

            if agent_index == 0:  # Agent's turn (maximizing player)
                legal_actions = state.get_agent_legal_actions()
                if len(legal_actions) == 0:
                    return float('-inf')

                best_value = float('-inf')
                best_action = None
                for action_index in legal_actions:
                    action = PlacementAction(index=action_index)
                    successor = state.generate_successor(agent_index, action)
                    value = expectimax(successor, depth + 1, 1, max_depth, max_actions)
                    if value > best_value:
                        best_value = value
                        best_action = action
                return best_action if depth == 0 else best_value

            else:  # Opponent's turn (expectation of random tile draw)
                legal_actions = np.array(state.get_opponent_legal_actions())
                if legal_actions.size == 0:
                    return float('-inf')

                num_actions = np.minimum(max_actions, len(legal_actions))
                tiles_indexes = np.random.choice(len(legal_actions), size=num_actions, replace=False)
                tiles = legal_actions[tiles_indexes]

                total_value = 0
                for tile in tiles:
                    successor = state.generate_successor(1, None)
                    successor.apply_opponent_action(tile)
                    value = expectimax(successor, depth + 1, 0, max_depth, max_actions)
                    total_value += value

                return total_value / num_actions if num_actions > 0 else 0

        # Adjust depth and number of actions dynamically based on the game state
        empty_tiles = len(game_state.get_empty_tiles())
        dynamic_depth = max(1, self.max_depth - (empty_tiles // 3.5))  # Increase depth as the board fills up
        dynamic_actions = max(1, self.max_actions - (empty_tiles // 1))  # Consider more actions as the game progresses

        # Measure running time for this method
        # start_time = time.time()
        best_action = expectimax(game_state, 0, 0, dynamic_depth, dynamic_actions)
        # end_time = time.time()

        # print(
        #     f"Expectimax running time (depth {dynamic_depth}, actions {dynamic_actions}): {end_time - start_time:.4f} seconds")

        if best_action is not None:
            return best_action
        return Action.STOP

    def default_evaluation_function(self, state):
        """Default evaluation function that returns the current score of the game state."""

        broken_sequences, empty_sequences, partial_sequences, duplicated_seqs = self.check_sequences(state)
        return (self.weights[4] * state.score -
                self.weights[0] * broken_sequences +
                self.weights[1] * empty_sequences +
                self.weights[2] * partial_sequences -
                self.weights[3] * duplicated_seqs)

    def check_sequences(self, state):
        # return 10, 10 , 10 ,10
        num_to_seq = np.zeros(9, dtype=int)
        empty_sequences = 0
        broken_sequences = 0
        partial_sequences = 0
        total_sum = 0
        # duplicated_seqs = 0
        # print("*")
        for seq, index in game_state.seq_to_idx.items():
            # print(seq)
            component_index = None
            if "_l" in seq:
                component_index = 2  # Right component
            elif "_d" in seq:
                component_index = 0  # Vertical component
            elif "_r" in seq:
                component_index = 1  # Left component

            # print(f"board index {state.board[index]}")
            # print(f"index: {index}")
            # mask = np.where(np.array(state.board[index]) != None)
            mask = ~np.isnan(state.board[index][:,0])
            # print(mask, "mask")
            filtered_list = state.board[index][mask][:, component_index].astype(int)
            # print(filtered_list, "filtered")
            # np.array([x for x in state.board[index] if x is not None]))
            # print(f"mask: {mask}")
            # filtered_values = state.board[index][mask][:, component_index]
            sum_values = np.sum(filtered_list)
            total_sum += sum_values
            unique_values = np.unique(filtered_list)
            different_values = unique_values.size
            if different_values > 0:
                # print(unique_values, "unique")
                num_to_seq[unique_values -1] += 1

            # sum_values = 0
            # unique_values = set()
            # for t in index:
            #     if state.board[t] is not None:
            #         # sum_values += state.board[t][component_index]
            #         unique_values.add(state.board[t][component_index])
            #         num_to_seq[state.board[t][component_index]] += 1
            #
            # # total_sum += sum_values
            # different_values = len(unique_values)

            if different_values > 1:
                broken_sequences += sum_values
            elif different_values == 1:
                partial_sequences += 1
            elif different_values == 0:
                empty_sequences += 1
            # duplicated_seqs += sum(i*num_to_seq[i] for i in range(10))

        broken_sequences /= total_sum
        empty_sequences /= len(game_state.seq_to_idx)
        partial_sequences /= len(game_state.seq_to_idx)
        duplicated_seqs = np.sum(np.arange(1,10)* num_to_seq)

        return broken_sequences, empty_sequences, partial_sequences, duplicated_seqs

    # def check_sequences(self, state):
    #     num_to_seq = np.zeros(9, dtype=int)
    #     empty_sequences = 0
    #     broken_sequences = 0
    #     partial_sequences = 0
    #     total_sum = 0
    #
    #     # Weighting factors for each number
    #     weight_factors = np.arange(1, 10)
    #
    #     for seq, indices in game_state.seq_to_idx.items():
    #         component_index = None
    #         if "_l" in seq:
    #             component_index = 2  # Left component
    #         elif "_d" in seq:
    #             component_index = 0  # Vertical component
    #         elif "_r" in seq:
    #             component_index = 1  # Right component
    #
    #         # Filter out empty slots (NaNs) for the current sequence
    #         mask = ~np.isnan(state.board[indices][:, 0])
    #         filtered_list = state.board[indices][mask][:, component_index].astype(int)
    #
    #         # Skip empty filtered lists
    #         if len(filtered_list) == 0:
    #             empty_sequences += 1
    #             continue
    #
    #         sum_values = np.sum(filtered_list)
    #         total_sum += sum_values
    #
    #         unique_values = np.unique(filtered_list)
    #         different_values = unique_values.size
    #
    #         # Ensure we align the bincount output with weight_factors
    #         bincount = np.bincount(filtered_list, minlength=10)[:9]  # Slice to match the shape of weight_factors
    #         weighted_sum = np.sum(weight_factors * bincount)
    #
    #         if different_values > 1:
    #             # Penalize broken sequences more heavily if they involve higher numbers
    #             broken_sequences += weighted_sum
    #         elif different_values == 1:
    #             # Reward partial sequences based on the value of the sequence
    #             partial_sequences += weighted_sum
    #             num_to_seq[unique_values[0] - 1] += 1
    #         elif different_values == 0:
    #             empty_sequences += 1
    #
    #     # Normalize sequences and penalties
    #     if total_sum > 0:
    #         broken_sequences /= total_sum
    #     empty_sequences /= len(game_state.seq_to_idx)
    #     partial_sequences /= len(game_state.seq_to_idx)
    #     duplicated_seqs = np.sum(weight_factors * num_to_seq)
    #
    #     return broken_sequences, empty_sequences, partial_sequences, duplicated_seqs
