from flask import Flask, request, jsonify
from query_processor import execute_search
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')  # Enable CORS for all origins

@app.route('/api/search', methods=['POST'])
def api():
    data = request.json

    if "searchText" in data and "country" in data and "isAuthorized" in data:
        search_query = data["searchText"].lower().strip()

        query_result = execute_search(search_query)

        response_data = {
            "searchText": data["searchText"],
            "country": data["country"],
            "isAuthorized": data["isAuthorized"],
            "queryResult": query_result
        }
        return jsonify(response_data)
    else:
        # If any of the required fields is missing, return an error response
        error_response = {"error": "Missing required fields"}
        return jsonify(error_response), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
