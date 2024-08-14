import numpy as np
import time
from game_state import GameState
from game import Game, RandomOpponentAgent
from MCTS_Agent import  MCTSAgent  # Assuming MCTSWithNetworks is defined in a file
from generate_data import load_networks
from expectimax_agent import Expectimax

def run_simulation(num_simulations=1000, output_file='mcts_scores.txt', policy_model_path='policy_network.h5', value_model_path='value_network.h5'):
    scores = []

    # Initialize the MCTS agent with the loaded networks
    mcts_agent = MCTSAgent(initial_simulations=400, final_simulations=600, exploration_weight=44.0)

    for i in range(num_simulations):
        start_time = time.time()  # Start the timer

        # Initialize the game state
        initial_state = GameState()

        # Create an opponent agent
        opponent_agent = RandomOpponentAgent()

        # Initialize the game
        game = Game(mcts_agent, opponent_agent)  # Use MCTS agent instead of Expectimax
        game.initialize(initial_state)

        # Run the game iteration by iteration
        while True:
            # Opponent's step: draw the current tile
            tile = game.current_tile()
            if tile is None:  # The game is finished
                break

            # Agent's step: choose the location to place the tile
            index = game.agent_location()
            if index is None:  # The game is finished
                break

        # Record the final score
        final_score = game._state.score
        scores.append(final_score)

        end_time = time.time()  # Stop the timer
        elapsed_time = end_time - start_time  # Calculate the elapsed time

        print(f"Simulation {i+1}: Final Score = {final_score}, Time: {elapsed_time:.4f} seconds")

    # Convert scores to a numpy array for easier statistical calculations
    scores = np.array(scores)

    # Calculate the expectation (mean) and standard deviation
    mean_score = np.mean(scores)
    std_dev = np.std(scores)

    # Write the scores, mean, and standard deviation to a file
    scores_array = np.array(scores)

    # Calculate the expectation (mean) and standard deviation
    mean_score = np.mean(scores_array)
    std_dev = np.std(scores_array)

    # Save the array of scores to a file in the format [2, 3, 4, ...]
    with open(output_file, 'w') as f:
        f.write(f"{scores_array.tolist()}\n")  # Save the array in a comma-separated list format
        f.write(f"\nExpectation (Mean): {mean_score}\n")
        f.write(f"Standard Deviation: {std_dev}\n")

    print(f"All {num_simulations} simulations completed.")
    print(f"Expectation (Mean) Score: {mean_score}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Scores and statistics saved to {output_file}.")
    print(f"Highest Score: {max(scores_array)}.")

    return scores_array


run_simulation(3)