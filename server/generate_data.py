import numpy as np

from MCTS_Agent import create_policy_network, create_value_network, MCTSNode, MCTSWithNetworks
from expectimax_agent import Expectimax
from game import RandomOpponentAgent, Game
from game_state import GameState
import tensorflow as tf

import numpy as np
import pickle

def generate_and_save_data(num_samples=1000, file_path='dataset.pkl', load = 0):
    data = generate_random_data(num_samples, load)

    # with open(file_path, 'wb') as f:
    #     pickle.dump(data, f)
    #
    # print(f"Dataset saved to {file_path}")
    return data

def generate_agent_policy_targets(game_state, agent):
    legal_moves = game_state.get_legal_actions()
    policy_target = np.zeros(19)

    if legal_moves:
        best_move = agent.get_action(game_state)
        policy_target[best_move.index] = 0.9 if len(legal_moves) > 1 else 1  # Assign a high probability to the chosen move

        remaining_prob = 0.1
        other_probs = remaining_prob / (len(legal_moves) - 1) if len(legal_moves) > 1 else 0
        policy_target[legal_moves] = np.maximum(policy_target[legal_moves], other_probs)
        # for move in legal_moves:
        #     if move != best_move.index:
        #         policy_target[move] = other_probs

    return policy_target

def generate_random_data(num_samples=1000, load=0):

    if load == 1:
        with open(f'{num_samples}_games_data.pkl', 'rb') as f:
            data = pickle.load(f)
            return data

    inputs = []
    policy_targets = []
    value_targets = []

    for _ in range(num_samples):
        game_state = GameState()  # Initialize a new game state
        agent = Expectimax(max_depth=3, max_actions=27)  # Assuming Expectimax is defined
        opponent_agent = RandomOpponentAgent()

        game = Game(agent, opponent_agent)
        game.initialize(game_state)

        while not game_state.done:
            # Record the current board state and current tile
            current_tile = game.current_tile()
            board_state = game_state.board  # Shape (19, 3)
            input_state = np.concatenate([board_state, np.array(current_tile).reshape(1, 3)], axis=0)  # Shape (20, 3)
            inputs.append(input_state)

            # Generate policy targets using the agent
            policy_target = generate_agent_policy_targets(game_state, agent)
            policy_targets.append(policy_target)

            # Agent's step: choose the location to place the tile
            index = game.agent_location()
            if index is None:
                break

        # Record the final score as the value target
        value_targets.append(game_state.score)

    inputs = np.array(inputs).reshape(len(inputs), 20, 3, 1)  # Shape (num_samples, 20, 3, 1)
    policy_targets = np.array(policy_targets)
    value_targets = np.array(value_targets).reshape(-1, 1)

    # save the samples
    data = {
        'input': inputs,
        'policy_target': policy_targets,
        'value_target': value_targets,
    }

    # Save the entire data structure to a file
    with open(f'{num_samples}_games_data.pkl', 'wb') as f:
        pickle.dump(data, f)

    return {data}

# generate_random_data()

def train_and_save_networks(policy_network, value_network, data, epochs=10, batch_size=32, policy_model_path='policy_network.h5', value_model_path='value_network.h5'):
    policy_network.compile(optimizer='adam', loss='categorical_crossentropy')
    value_network.compile(optimizer='adam', loss='mean_squared_error')

    policy_network.fit(data['input'], data['policy_target'], epochs=epochs, batch_size=batch_size)
    value_network.fit(data['input'], data['value_target'], epochs=epochs, batch_size=batch_size)

    # Save the trained models
    policy_network.save(policy_model_path)
    value_network.save(value_model_path)

    print(f"Policy network saved to {policy_model_path}")
    print(f"Value network saved to {value_model_path}")

def load_networks(policy_model_path='policy_network.h5', value_model_path='value_network.h5'):
    policy_network = tf.keras.models.load_model(policy_model_path)
    value_network = tf.keras.models.load_model(value_model_path)

    print(f"Policy network loaded from {policy_model_path}")
    print(f"Value network loaded from {value_model_path}")

    return policy_network, value_network

if __name__ == "__main__":
    # # Step 1: Generate and save the dataset
    # data = generate_and_save_data(num_samples=1000, file_path='dataset.pkl',load=1) #load samples from pkl file
    # data['value_target'] = np.repeat(data['value_target'], 19)
    # data['input'] = np.nan_to_num(data['input'], nan=0.0) #consider moving it to the generation
    # print("Data Generated")
    # # Step 2: Create and train networks, then save them
    # input_shape = (20, 3, 1)
    # policy_network = create_policy_network(input_shape)
    # value_network = create_value_network(input_shape)
    # train_and_save_networks(policy_network, value_network, data, epochs=10, batch_size=32, policy_model_path='policy_network.h5', value_model_path='value_network.h5')
    # print("Models Trained")

    # Step 3: Load the trained models
    policy_network, value_network = load_networks(policy_model_path='policy_network.h5', value_model_path='value_network.h5')

    # # Step 4: Run MCTS with the loaded models
    # initial_state = GameState()
    # root = MCTSNode(initial_state)
    # mcts_agent = MCTSWithNetworks(policy_network, value_network)
    # best_action = mcts_agent.search(root)

    # Initialize the game state
    initial_state = GameState()
    root = MCTSNode(initial_state)
    mcts_agent = MCTSWithNetworks(policy_network, value_network)

    opponent_agent = RandomOpponentAgent()

    # Initialize the game
    game = Game(mcts_agent, opponent_agent)
    game.initialize(initial_state)
    game.current_tile()
    best_action = mcts_agent.search(root)

    print(f"Best action chosen by MCTS: {best_action.index}")
