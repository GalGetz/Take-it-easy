from flask import Flask, request, jsonify 
from flask_cors import CORS
from game import Game, RandomOpponentAgent
from game_state import GameState
from agent_factory import AgentFactory
import threading
import json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

manager = None
class GameManager:
    def __init__(self, agent):
        # Initialize the game state
        self._initial_state = GameState()

        # Initialize the agents
        self._agent = AgentFactory.create_agent(agent)
        self._opponent_agent = RandomOpponentAgent()

        # Initialize the game
        self._game = Game(self._agent, self._opponent_agent)
        self._game.initialize(self._initial_state)

        # Prepare a list to store calculated turns
        self.turns = []
        self.lock = threading.Lock()
        self.user_turn_index = 0
        print("start threads")
        # Start the background thread to calculate agent moves
        self.thread = threading.Thread(target=self.calculate_moves)
        self.thread.start()
        print("finished init")

    def calculate_moves(self):
        t = 0
        while t < 19:
            self._curr_tile = self._game.current_tile()
            self._agent_loc = self._game.agent_location()
            self.turns.append((self._curr_tile, self._agent_loc))
            print((self._curr_tile, self._agent_loc))
            print("computed ",t)
            t += 1

    def get_turn(self):
        if self.user_turn_index < len(self.turns):
            return self.turns[self.user_turn_index]
        else:
            return None, None

    def get_agent_score(self):
        return self._game._state.score

    def get_user_score(self, board):
        return GameState.calculate_score(board)


@app.route('/init_game', methods=['POST'])
def init_game():
    data = request.get_json()

    global manager
    manager = GameManager(data['agent'])
    print(data["agent"])

    return jsonify({'status': 'success', 'message': f'Game initialized with agent{data["agent"]}'})


@app.route('/rest_tiles', methods=['GET'])
def rest_tiles():
    state = GameState()
    tiles = state.generate_tiles()

    response = {
        'status': 'success',
        'data': tiles,
    }
    return jsonify(response)

@app.route('/current_tile', methods=['GET'])
def current_tile():
    tile, _ = manager.get_turn()

    while tile is None:
        tile, _ = manager.get_turn()

    response = {
        'status': 'success',
        'data': tile,
    }
    return jsonify(response)


@app.route('/agent_location', methods=['GET'])
def agent_location():
    _, location = manager.get_turn() #0 for tests

    while location is None:
        _, location = manager.get_turn()

    response = {
        'status': 'success',
        'data': location,
    }
    manager.user_turn_index += 1
    return jsonify(response)

@app.route('/scores', methods=['GET'])
def scores():
    tiles = request.args.get('tiles')
    board = json.loads(tiles)
    agent_score = manager.get_agent_score()
    user_score = manager.get_user_score(board)
    response = {
        'status': 'success',
        'agent_score': int(agent_score),
        'user_score' : int(user_score)
    }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)