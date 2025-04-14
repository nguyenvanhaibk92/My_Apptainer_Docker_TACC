# gene_api.py
from flask import Flask, request, jsonify
import redis
import requests
import json

app = Flask(__name__)

# Redis host will be "redis" in Docker Compose
# line with "localhost" was for testing before dockerizing the application
#r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(host='redis', port=6379, decode_responses=True)
# Direct JSON file
HGNC_URL = "https://storage.googleapis.com/public-download-files/hgnc/json/json/hgnc_complete_set.json"

@app.route('/data', methods=['POST'])
def load_data() -> tuple[str, int]:
    """
    Download HGNC JSON and load it into Redis.
    """
    try:
        resp = requests.get(HGNC_URL)
        data = resp.json()  # Will raise an error if not valid JSON

        for entry in data['response']['docs']:
            hgnc_id = entry.get('hgnc_id')
            if hgnc_id:
                r.set(hgnc_id, json.dumps(entry))

        return 'Data loaded into Redis\n', 200

    except requests.exceptions.RequestException as e:
        return f"Request error: {e}\n", 500
    except json.JSONDecodeError:
        return "Error: Failed to parse JSON\n", 500
    except Exception as e:
        return f"Unexpected error: {e}\n", 500

@app.route('/data', methods=['GET'])
def get_all_data() -> tuple[str, int]:
    """
    Return all Redis data as JSON.
    """
    try:
        keys = r.keys("HGNC:*")
        all_data = [json.loads(r.get(k)) for k in keys]
        return jsonify(all_data), 200
    except Exception as e:
        return f"Error: {e}\n", 500

@app.route('/data', methods=['DELETE'])
def delete_all_data() -> tuple[str, int]:
    """
    Delete all data from Redis.
    """
    try:
        keys = r.keys("HGNC:*")
        for key in keys:
            r.delete(key)
        return 'All HGNC data deleted from Redis\n', 200
    except Exception as e:
        return f"Error: {e}\n", 500

@app.route('/genes', methods=['GET'])
def list_gene_ids() -> tuple[str, int]:
    """
    List all HGNC IDs stored in Redis.
    """
    try:
        keys = r.keys("HGNC:*")
        return jsonify(keys), 200
    except Exception as e:
        return f"Error: {e}\n", 500

@app.route('/genes/<hgnc_id>', methods=['GET'])
def get_gene_by_id(hgnc_id: str) -> tuple[str, int]:
    """
    Return data for a given HGNC ID.
    """
    try:
        data = r.get(hgnc_id)
        if data:
            return jsonify(json.loads(data)), 200
        else:
            return f"HGNC ID '{hgnc_id}' not found.\n", 404
    except Exception as e:
        return f"Error: {e}\n", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

