# import necessary modules
import sys
import numpy as np
from skopt import gp_minimize
from skopt.space import Real
from skopt.utils import use_named_args

from game_state import GameState
from game import Game, RandomOpponentAgent
from expectimax_agent import Expectimax


# Function to run the simulation
def run_simulation(weights, num_simulations=25):
    scores = []

    for _ in range(num_simulations):
        # Initialize the game state
        initial_state = GameState()

        # Create the agent and opponent agent
        agent = Expectimax(weights=weights, max_depth=4, max_actions=27)
        opponent_agent = RandomOpponentAgent()

        # Initialize the game
        game = Game(agent, opponent_agent)
        game.initialize(initial_state)

        # Run the game iteration by iteration
        while not game._state.done:
            tile = game.current_tile()
            if tile is None:
                break

            index = game.agent_location()
            if index is None:
                break

        # Record the final score
        final_score = game._state.score
        scores.append(final_score)

    # Convert scores to a numpy array for easier statistical calculations
    scores = np.array(scores)

    # Calculate the expectation (mean) and standard deviation
    mean_score = np.mean(scores)
    std_dev = np.std(scores)

    return mean_score, std_dev


# Optimization function
def run_simulation_with_weights(weights):
    mean_score, std_dev = run_simulation(weights)
    return -mean_score  # Negate because Bayesian optimization minimizes the objective function


# Define the search space for the weights
space = [
    Real(0.01, 10.0, name='broken_seq_weight'),
    Real(0.01, 10.0, name='empty_seq_weight'),
    Real(0.01, 10.0, name='partial_seq_weight'),
    Real(0.01, 10.0, name='duplicated_seq_weight'),
    Real(0.01, 10.0, name='score_weight')
]


@use_named_args(space)
def objective(**weights):
    return run_simulation_with_weights(list(weights.values()))


if __name__ == "__main__":
    # Perform Bayesian optimization with progress tracking
    n_calls = 50
    print(f"Starting Bayesian optimization with {n_calls} iterations...\n")
    res = gp_minimize(objective, space, n_calls=n_calls, random_state=0, verbose=True)

    # Print the best weights and the corresponding score
    print("\nOptimization complete!")
    print("Best weights found: ", res.x)
    print("Best score achieved: ", -res.fun)

    # Print the progress
    for i, (weights, score) in enumerate(zip(res.x_iters, res.func_vals), 1):
        print(f"Iteration {i}/{n_calls}: Weights = {weights}, Score = {-score:.4f}")
