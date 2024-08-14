from MCTS_Agent import create_policy_network, create_value_network, MCTSNode, MCTSWithNetworks
from generate_data import train_and_save_networks, load_networks
import numpy as np
import pickle

# files = ["2000_games_data.pkl","1000_games_data_20240814_124851_4.pkl", "2000_games_data_20240814_120922_4.pkl",
# "10000_games_data_20240814_133808_3.pkl\\10000_games_data_20240814_133808_3.pkl"]
# input_shape = (20, 3, 1)
# # policy_network = create_policy_network(input_shape)
# value_network = create_value_network(input_shape)
#
# with open(files[0], 'rb') as f:
#     data = pickle.load(f)
#     inputs = data['input']
#     policy_targets = data['policy_target']
#     value_targets = data['value_target']
#
#
# for file in files[1:]:
#     with open(file, 'rb') as f:
#         data = pickle.load(f)
#         inputs = np.concatenate([inputs, data['input']], axis=0)
#         policy_targets = np.concatenate([policy_targets, data['policy_target']], axis=0)
#         value_targets = np.concatenate([value_targets, data['value_target']], axis=0)
#
# data = {
#     'input': inputs,
#     'policy_target': policy_targets,
#     'value_target': value_targets,
# }
# data['value_target'] = np.repeat(data['value_target'], 19)
# data['input'] = np.nan_to_num(data['input'], nan=0.0) #consider moving it to the generation

file = "5000_games_data_20240814_134558.pkl"
policy_network, value_network = load_networks(policy_model_path='policy_network.h5', value_model_path='value_network.h5')
with open(file, 'rb') as f:
    data = pickle.load(f)
    inputs = data['input']
    policy_targets = data['policy_target']
    value_targets = data['value_target']
data['value_target'] = np.repeat(data['value_target'], 19)
data['input'] = np.nan_to_num(data['input'], nan=0.0)

train_and_save_networks(policy_network, value_network, data, epochs=10, batch_size=32, policy_model_path='policy_network.h5', value_model_path='value_network.h5')
print("Models Trained")