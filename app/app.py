from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route('/')
def index():
    return jsonify({"Message": "Hello World"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)