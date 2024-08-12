from random_agent import RandomAgent
from expectimax_agent import Expectimax


class AgentFactory:
    @staticmethod
    def create_agent(agent_type_str: str):
        if agent_type_str == "Random":
            return RandomAgent()
        elif agent_type_str == "Expectimax":
            return Expectimax(depth=2)
        else:
            raise ValueError(f"Unknown agent type: {agent_type_str}")
