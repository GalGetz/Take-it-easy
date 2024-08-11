from game import Agent
import game_state

class Expectimax(Agent):
    def __init__(self, depth=3, evaluation_function=None):
        super(Expectimax, self).__init__()
        self.depth = depth
        self.evaluation_function = evaluation_function if evaluation_function else self.default_evaluation_function

    def get_action(self, game_state, tile):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        The opponent is modeled as choosing uniformly at random from their legal moves.
        """
        def expectimax(state, depth, agent_index):
            if state.done or depth == self.depth:
                return self.evaluation_function(state)

            legal_actions = state.get_legal_actions()
            if agent_index == 0:  # Agent's turn (maximizing player)
                best_value = float('-inf')
                for action in legal_actions:
                    successor = state.generate_successor(action, tile)
                    value = expectimax(successor, depth, 1)
                    best_value = max(best_value, value)
                return best_value
            else:  # Opponent's turn (expectation of random board response)
                total_value = 0
                num_actions = len(legal_actions)
                for action in legal_actions:
                    successor = state.generate_successor(action, tile)
                    value = expectimax(successor, depth + 1, 0)
                    total_value += value
                return total_value / num_actions if num_actions > 0 else 0

        best_score = float('-inf')
        best_action = None
        for action in game_state.get_legal_actions():
            successor = game_state.generate_successor(action, tile)
            score = expectimax(successor, 0, 1)
            if score > best_score:
                best_score = score
                best_action = action

        return best_action

    def default_evaluation_function(self, state):
        """Default evaluation function that returns the current score of the game state."""
        return state.score

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
