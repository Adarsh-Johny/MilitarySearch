from flask import Blueprint, request, jsonify
from MilitaryDefenseApp.search.query_processor import execute_search

search_blueprint = Blueprint('search', __name__)

@search_blueprint.route('/', methods=['POST'])
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
