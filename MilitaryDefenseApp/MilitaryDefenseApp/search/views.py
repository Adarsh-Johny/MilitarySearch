from django.http import HttpResponse
from django.shortcuts import render
from SPARQLWrapper import SPARQLWrapper, JSON

def search(request):
    # Specify the DBpedia endpoint
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    # Define your SPARQL query to retrieve military information
    query = """
        SELECT ?commander
        WHERE {
            dbr:United_States_Armed_Forces dbp:commander ?commander.
        }
    """

    # Set the SPARQL query and execute it
    sparql.setQuery(query)
    results = sparql.query().convert()

    # Extract relevant information from the query results
    commanders = [result["commander"]["value"] for result in results["results"]["bindings"]]

    # Construct a response with the military units as content
    response_content = "\n".join(commanders)
    response = HttpResponse(response_content, content_type="text/plain")

    return response

