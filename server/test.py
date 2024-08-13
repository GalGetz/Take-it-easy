import numpy as np
import time
from game_state import GameState
from game import Game, RandomOpponentAgent
from MCTS_Agent import MCTSWithNetworks  # Assuming MCTSWithNetworks is defined in a file
from generate_data import load_networks
def run_simulation(num_simulations=100, output_file='mcts_scores.txt', policy_model_path='policy_network.h5', value_model_path='value_network.h5'):
    scores = []

    # Load the trained policy and value networks
    policy_network = load_networks(policy_model_path)
    value_network = load_networks(value_model_path)

    # Initialize the MCTS agent with the loaded networks
    mcts_agent = MCTSWithNetworks(policy_network, value_network, exploration_weight=1.0, simulations_number=1000)

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
    with open(output_file, 'w') as f:
        for score in scores:
            f.write(f"{score}\n")
        f.write(f"\nExpectation (Mean): {mean_score}\n")
        f.write(f"Standard Deviation: {std_dev}\n")

    print(f"All {num_simulations} simulations completed.")
    print(f"Expectation (Mean) Score: {mean_score}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Scores and statistics saved to {output_file}.")
    print(f"Highest {max(scores)}.")

    return mean_score, std_dev
