import json

from flask import Flask, jsonify, send_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, world!\n'

@app.route('/<name>', methods=['GET'])
def hello_name(name):
    return f'Hello, {name}!\n'

# Method 1: Return JSON directly
@app.route('/download/json1', methods=['GET'])
def download_json1():
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    # This will return JSON with proper headers
    return jsonify(data)

# Method 2: Send a physical JSON file
# ! this is to download the file to the current directory
# ! Downloads a file named data.json
# ! curl -O http://localhost:5000/download/json2

@app.route('/download/json2', methods=['GET'])
def download_json2():
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    
    # First write the data to a file
    with open('data.json', 'w') as f:
        json.dump(data, f)
    
    # Return the file with proper MIME type
    return send_file('data.json', mimetype='application/json')



# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
