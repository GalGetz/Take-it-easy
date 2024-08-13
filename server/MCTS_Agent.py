import math
import random

from game import Agent, PlacementAction


class MCTSNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.children = []
        self.visits = 0
        self.value = 0.0

    def is_fully_expanded(self):
        return len(self.children) == len(self.state.get_agent_legal_actions())

    def best_child(self, exploration_weight=1.0):
        # UCB1 formula
        choices_weights = [
            (child.value / child.visits) + exploration_weight * math.sqrt(2 * math.log(self.visits) / child.visits)
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]

    def expand(self):
        legal_actions = self.state.get_agent_legal_actions()
        for action in legal_actions:
            if not any(child.action.index == action for child in self.children):
                next_state = self.state.generate_successor(agent_index=0, action=PlacementAction(index=action))
                child_node = MCTSNode(next_state, parent=self, action=PlacementAction(index=action))
                self.children.append(child_node)
                return child_node

    def best_action(self):
        return max(self.children, key=lambda child: child.visits).action


class MCTS:
    def __init__(self, exploration_weight=1.0, simulations_number=1000):
        self.exploration_weight = exploration_weight
        self.simulations_number = simulations_number

    def search(self, root):
        for _ in range(self.simulations_number):
            node = self.select(root)
            if not node.state.done:  # Expand only if not a terminal state
                node = node.expand()
            reward = self.simulate(node.state)
            self.backpropagate(node, reward)
        return root.best_action()

    def select(self, node):
        while not node.state.done:
            if node.is_fully_expanded():
                node = node.best_child(self.exploration_weight)
            else:
                return node
        return node

    def simulate(self, state):
        # Simulate a random rollout from the current state
        while not state.done:
            # Generate a tile using the opponent's logic
            opponent_action = state.pop_random_tile(random.randint(0, len(state.tiles) - 1))
            state.apply_opponent_action(opponent_action)

            # If the game is done after the opponent's action, break out of the loop
            if state.done:
                break

            # Get legal actions for the agent and randomly choose one
            legal_actions = state.get_agent_legal_actions()
            action = random.choice(legal_actions)
            state = state.generate_successor(agent_index=0, action=PlacementAction(index=action))

        return state.score  # Return the game score after the simulation ends

    def backpropagate(self, node, reward):
        while node is not None:
            node.visits += 1
            node.value += reward
            node = node.parent


class MCTSAgent(Agent):
    def __init__(self, initial_simulations=100, final_simulations=1000, exploration_weight=1.0, max_steps=19):
        super(MCTSAgent, self).__init__()
        self.initial_simulations = initial_simulations
        self.final_simulations = final_simulations
        self.exploration_weight = exploration_weight
        self.max_steps = max_steps

    def get_action(self, game_state):
        current_step = self.max_steps - len(game_state.get_empty_tiles())
        simulations_number = self.adjust_simulations(current_step)
        root = MCTSNode(game_state)
        mcts = MCTS(exploration_weight=self.exploration_weight, simulations_number=simulations_number)
        return mcts.search(root)

    def adjust_simulations(self, current_step):
        """Adjust the number of simulations based on the current step of the game."""
        return int(self.initial_simulations + (self.final_simulations - self.initial_simulations) * (
                    current_step / self.max_steps))