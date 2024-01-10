from SPARQLWrapper import JSON, SPARQLWrapper
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


@app.route('/api/list', methods=['GET'])
def api_country_wise_list():
    
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        SELECT ?country ?militaryForce
        WHERE {{
          ?militaryForce rdf:type dbo:MilitaryUnit.
          ?militaryForce dbo:country ?countryResource.
          ?countryResource rdfs:label ?country.
          FILTER(LANG(?country) = "en")
        }}
        ORDER BY ?country
    """

    sparql.setQuery(query)
    results = sparql.query().convert()
    military_forces_list = []
    for result in results["results"]["bindings"]:
        country = result["country"]["value"]
        military_force = result["militaryForce"]["value"]
        military_forces_list.append({"Country": country, "Url": military_force})

    return jsonify(military_forces_list)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
