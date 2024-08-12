from game import Agent, Action, PlacementAction
import game_state


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
                legal_actions = state.get_opponent_legal_actions()
                total_value = 0
                num_actions = len(legal_actions)
                for tile in legal_actions:
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

        broken_sequences, empty_sequences, partial_sequences = self.check_sequences(state)
        return state.score - broken_sequences*10 + empty_sequences*10 + partial_sequences*10

    def check_sequences(self, state):
        empty_sequences = 0
        broken_sequences = 0
        partial_sequences = 0
        for seq in game_state.seq_to_idx.values():
            component_index = None
            if "_l" in seq:
                component_index = 2  # Right component
            elif "_d" in seq:
                component_index = 0  # Vertical component
            elif "_r" in seq:
                component_index = 1  # Left component

            filtered_values = [state.board[t][component_index] for t in seq if state.board[t] is not None]
            different_values = len(set(filtered_values))
            if different_values > 1:
                #every location belongs to 3 sequences
                broken_sequences += len(seq)
            elif different_values == 1:
                partial_sequences += 1
            elif len(filtered_values) == 0:
                empty_sequences += 1

        broken_sequences /= (3* game_state.DEFAULT_BOARD_SIZE)
        empty_sequences /= len(game_state.seq_to_idx)
        partial_sequences /= len(game_state.seq_to_idx)

        return broken_sequences,empty_sequences, partial_sequences
