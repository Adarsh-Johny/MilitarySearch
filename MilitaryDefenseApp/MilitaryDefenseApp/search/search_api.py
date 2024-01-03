from flask import Flask, request, jsonify
from query_processor import execute_search

app = Flask(__name__)

@app.route('/api/search', methods=['POST'])
def api():
    data = request.json

    if "searchText" in data and "Country" in data and "isAuthorized" in data:
        search_query = data["searchText"].lower().strip()

        query_result = execute_search(search_query)

        response_data = {
            "searchText": data["searchText"],
            "Country": data["Country"],
            "isAuthorized": data["isAuthorized"],
            "queryResult": query_result
        }
        return jsonify(response_data)
    else:
        # If any of the required fields is missing, return an error response
        error_response = {"error": "Missing required fields"}
        return jsonify(error_response), 400


@app.route('/api/abc', methods=['GET'])
def api2():
    return jsonify("response_data")

if __name__ == '__main__':
    app.run(debug=True)
