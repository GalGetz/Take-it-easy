from flask import Flask, request, jsonify 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


data = {'current': [],
         'tiles': []}

@app.route('/data', methods=['GET'])
def get_data():
    response = {
        'status': 'success',
        'data': data,
    }
    return jsonify(response)

@app.route('/data', methods=['POST'])
def post_data():
    json = request.get_json()
    data['current'] = json['current']
    data['tiles'] = json['tiles']
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)