from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')  # Enable CORS for all origins

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)