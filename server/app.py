from flask import Flask, request, jsonify 
from flask_cors import CORS
from game import Game, RandomOpponentAgent
from game_state import GameState
from agent_factory import AgentFactory
import threading

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

manager = None
class GameManager:
    def __init__(self, agent):
        # Initialize the game state
        self._initial_state = GameState()

        # Initialize the agents
        self._agent = AgentFactory.create_agent(agent)
        self._opponent_agent = RandomOpponentAgent()

        # Initialize the game
        self._game = Game(agent, self._opponent_agent)
        self._game.initialize(self._initial_state)

        # Prepare a list to store calculated turns
        self.turns = []
        self.lock = threading.Lock()
        self.user_turn_index = 0

        # Start the background thread to calculate agent moves
        self.thread = threading.Thread(target=self.calculate_moves)
        self.thread.start()

    def calculate_moves(self):
        while True:
            with self.lock:
                # Calculate the next turn
                self._curr_tile = self._game.current_tile()
                self._agent_loc = self._game.agent_location(self._curr_tile)
                self.turns.append((self._curr_tile, self._agent_loc))

    def get_turn(self):
        with self.lock:
            if self.user_turn_index < len(self.turns):
                return self.turns[self.user_turn_index]
            else:
                return None, None




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

@app.route('/agent_score', methods=['GET'])
def agent_score():
    score = -1 # for tests
    response = {
        'status': 'success',
        'data': score,
    }
    return jsonify(response)

@app.route('/init_game', methods=['POST'])
def init_game():
    data = request.get_json()

    global manager
    manager = GameManager(data['agent'])

    return jsonify({'status': 'success', 'message': f'Game initialized with agent{data["agent"]}'})

if __name__ == '__main__':
    app.run(debug=True)