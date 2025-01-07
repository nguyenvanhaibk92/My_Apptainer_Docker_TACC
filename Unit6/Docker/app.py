import json

import redis
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_redis_client():
    """Create and return a Redis client"""
    return redis.Redis(host='redis-db', port=6379, db=0)

rd = get_redis_client()

@app.route('/data', methods=['POST', 'GET', 'DELETE'])
def handle_data():
    """Handle all operations for meteorite landings data"""
    
    if request.method == 'POST':
        # Get data from the URL
        response = requests.get('https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json')
        data = response.json()
        
        # Store each meteorite as a hash in Redis
        # Using meteorite ID as key
        for meteorite in data['meteorite_landings']:
            key = f"meteorite:{meteorite['id']}"
            rd.hmset(key, meteorite)
            
        return jsonify({"message": "Data loaded successfully"}), 201
        
    elif request.method == 'GET':
        # Retrieve all meteorite keys
        keys = rd.keys('meteorite:*')
        meteorites = []
        
        # Get data for each meteorite
        for key in keys:
            meteorite_data = rd.hgetall(key)
            # Convert bytes to string for each field
            meteorite = {k.decode('utf-8'): v.decode('utf-8') 
                        for k, v in meteorite_data.items()}
            meteorites.append(meteorite)
            
        return jsonify({"meteorite_landings": meteorites}), 200
        
    elif request.method == 'DELETE':
        # Delete all meteorite keys
        keys = rd.keys('meteorite:*')
        for key in keys:
            rd.delete(key)
            
        return jsonify({"message": "All data deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)