from random_agent import RandomAgent
from expectimax_agent import Expectimax
from MCTS_Agent import MCTSAgent


class AgentFactory:
    @staticmethod
    def create_agent(agent_type_str: str):
        if agent_type_str == "Random":
            return RandomAgent()
        elif agent_type_str == "Expectimax":
            return Expectimax(depth=2)
        elif agent_type_str == "Monte Carlo":
            return MCTSAgent(800, final_simulations=1000, exploration_weight=7.0)
        else:
            raise ValueError(f"Unknown agent type: {agent_type_str}")
