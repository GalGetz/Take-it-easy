from flask import Flask, request, jsonify 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


data = {'current': [],
         'tiles': []}



@app.route('/current_tile', methods=['GET'])
def current_tile():
    tile = [1,1,1] # for tests
    response = {
        'status': 'success',
        'data': tile,
    }
    return jsonify(response)

@app.route('/agent_location', methods=['GET'])
def agent_location():
    location = 0 # for tests
    response = {
        'status': 'success',
        'data': location,
    }
    return jsonify(response)

@app.route('/agent_score', methods=['GET'])
def agent_score():
    score = -1 # for tests
    response = {
        'status': 'success',
        'data': score,
    }
    return jsonify(response)

@app.route('/set_agent', methods=['POST'])
def set_agent():
    json = request.get_json()
    data['current'] = json['current']
    data['tiles'] = json['tiles']
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)