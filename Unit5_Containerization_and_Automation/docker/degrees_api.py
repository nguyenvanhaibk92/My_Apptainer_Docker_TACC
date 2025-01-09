import json

import yaml
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_config():
    default_config = {"debug": True}
    try:
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Couldn't load the config file; details: {e}")
    # if we couldn't load the config file, return the default config
    return default_config

# @app.route('/degrees', methods=['GET'])
def get_data():
    data = [ {'id': 0, 'year': 1990, 'degrees': 5818},
             {'id': 1, 'year': 1991, 'degrees': 5725},
             {'id': 2, 'year': 1992, 'degrees': 6005},
             {'id': 3, 'year': 1993, 'degrees': 6123},
             {'id': 4, 'year': 1994, 'degrees': 6096} ]
    return data
    
@app.route('/degrees/<id>', methods=['GET'])
def degrees_for_id(id):
    try:
        # Convert string id to integer
        id_num = int(id)
        
        # Get data and search for matching id
        data = get_data()
        
        for item in data:
            if item["id"] == id_num:
                return item
        
        # If we get here, id wasn't found
        return jsonify({"error": f"No degree data found for id {id}"}), 404

    except ValueError:
        # Handle case where id cannot be converted to int
        return jsonify({"error": "Invalid id parameter; id must be an integer"}), 400

@app.route('/degrees/<id>/degrees', methods=['GET'])
def degrees_for_id_degree(id):
    try:
        # Convert string id to integer
        id_num = int(id)
        
        # Get data and search for matching id
        data = get_data()
        
        for item in data:
            if item["id"] == id_num:
                return jsonify(item["degrees"])
        
        # If we get here, id wasn't found
        return jsonify({"error": f"No degree data found for id {id}"}), 404

    except ValueError:
        # Handle case where id cannot be converted to int
        return jsonify({"error": "Invalid id parameter; id must be an integer"}), 400
    
@app.route('/degrees', methods=['GET'])
def degrees():
    start = request.args.get('start', 0)
    if not start.isnumeric():
        return "Error: start must be an integer"
    start = int(start)
    data = get_data()
    result = []
    for d in data:
        if d['year'] >= start:
            result.append(d)
    return result

# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    config = get_config()
    if config.get('debug', True):
        app.run(debug=True, host='0.0.0.0')
    else:
        app.run(host='0.0.0.0')
    
# curl http://localhost:5000/degrees?start=1993