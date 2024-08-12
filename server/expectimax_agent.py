import itertools

from game import Agent, Action, PlacementAction
import game_state
import numpy as np


class Expectimax(Agent):
    def __init__(self, depth=3, evaluation_function=None):
        super(Expectimax, self).__init__()
        self.depth = depth
        self.evaluation_function = evaluation_function if evaluation_function else self.default_evaluation_function


    def get_action(self, game_state):
        """
        Returns the expectimax action using self.depth and self.evaluation_function.

        The opponent is modeled as choosing uniformly at random from their legal moves.
        """
        def expectimax(state, depth, agent_index):
            if state.done or depth == self.depth:
                return self.evaluation_function(state)
            if agent_index == 0:  # Agent's turn (maximizing player)
                legal_actions = state.get_agent_legal_actions()
                best_value = float('-inf')
                best_action = None
                for action_index in legal_actions:
                    action = PlacementAction(index=action_index)
                    successor = state.generate_successor(agent_index, action)
                    value = expectimax(successor, depth, 1)
                    if value > best_value:
                        best_value = value
                        best_action = action
                return best_action if depth == 0 else best_value
            else:  # Opponent's turn (expectation of random tile draw)
                legal_actions = np.array(state.get_opponent_legal_actions())
                total_value = 0
                num_actions = np.minimum(10,len(legal_actions))
                tiles_indexes = np.random.choice(len(legal_actions), size=num_actions, replace=False)
                tiles = legal_actions[tiles_indexes]
                # legal = list(itertools.permutations(legal_actions))[:10] if len(legal_actions) > 10 else legal_actions
                for tile in tiles:
                    # tile = legal_actions[np.random(len(legal_actions))]
                    successor = state.generate_successor(1, None)
                    successor.apply_opponent_action(tile)
                    value = expectimax(successor, depth + 1, 0)
                    total_value += value
                return total_value / num_actions if num_actions > 0 else 0
        best_action = expectimax(game_state, 0, 0)
        if best_action is not None:
            return best_action
        return Action.STOP


    def default_evaluation_function(self, state):
        """Default evaluation function that returns the current score of the game state."""

        broken_sequences, empty_sequences, partial_sequences, duplicated_seqs = self.check_sequences(state)
        return state.score - broken_sequences*10 + empty_sequences*10 + partial_sequences*10 - duplicated_seqs

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
