from random_agent import RandomAgent
from expectimax_agent import Expectimax
from MCTS_Agent import MCTSAgent


class AgentFactory:
    @staticmethod
    def create_agent(agent_type_str: str):
        if agent_type_str == "Random":
            return RandomAgent()
        elif agent_type_str == "Expectimax":
            return Expectimax(max_depth=4, max_actions=27, weights=[10.0, 10.0, 2.736195488285202, 0.01, 0.01])
        elif agent_type_str == "Monte Carlo":
            return MCTSAgent(initial_simulations=400, final_simulations=600, exploration_weight=40.0)
        else:
            raise ValueError(f"Unknown agent type: {agent_type_str}")
