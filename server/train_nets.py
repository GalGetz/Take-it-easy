from MCTS_Agent import create_policy_network, create_value_network, MCTSNode, MCTSWithNetworks
from generate_data import train_and_save_networks
import numpy as np
import pickle

filename = ""
input_shape = (20, 3, 1)
policy_network = create_policy_network(input_shape)
value_network = create_value_network(input_shape)

with open(filename, 'rb') as f:
    data = pickle.load(f)



train_and_save_networks(policy_network, value_network, data, epochs=10, batch_size=32, policy_model_path='policy_network.h5', value_model_path='value_network.h5')
print("Models Trained")