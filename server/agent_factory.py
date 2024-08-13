from random_agent import RandomAgent
from expectimax_agent import Expectimax
from MCTS_Agent import MCTSAgent


class AgentFactory:
    @staticmethod
    def create_agent(agent_type_str: str):
        if agent_type_str == "Random":
            return RandomAgent()
        elif agent_type_str == "Expectimax":
            return Expectimax(max_depth=6, max_actions=27, weights=[39.42971357026892, 23.574126129258843, 4.781886656778408, 2.2942174213455666, 3.209554048482536])
        elif agent_type_str == "Monte Carlo":
            return MCTSAgent(initial_simulations=800, final_simulations=5000, exploration_weight=80.0)
        else:
            raise ValueError(f"Unknown agent type: {agent_type_str}")
