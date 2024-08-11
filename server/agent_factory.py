from random_agent import RandomAgent


class AgentFactory:
    @staticmethod
    def create_agent(agent_type_str: str):
        if agent_type_str == "Random":
            return RandomAgent()
        elif agent_type_str == "A-star":
            pass
            # return AStarAgent()
        elif agent_type_str == "RL":
            # return ReinforcementLearningAgent()
            pass
        elif agent_type_str == "Monte Carlo":
            pass
            # return MonteCarloAgent()
        else:
            raise ValueError(f"Unknown agent type: {agent_type_str}")
