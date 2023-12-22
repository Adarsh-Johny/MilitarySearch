from django.http import HttpResponse
from django.shortcuts import render
from SPARQLWrapper import SPARQLWrapper, JSON

def search(request):
    # Specify the DBpedia endpoint
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    # Define your SPARQL query to retrieve military information
    query = """
        PREFIX dbres: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        
        SELECT DISTINCT ?militaryResource ?militaryResourceLabel
        WHERE {
            ?militaryResource a dbo:MilitaryUnit .
            ?militaryResource rdfs:label ?militaryResourceLabel
            FILTER(LANG(?militaryResourceLabel) = "" || LANG(?militaryResourceLabel) = "en")
        }
        LIMIT 10
    """

    # Set the SPARQL query and execute it
    sparql.setQuery(query)
    results = sparql.query().convert()

    # Extract relevant information from the query results
    military_units = []
    for result in results["results"]["bindings"]:
        military_units.append(result["militaryResourceLabel"]["value"])

    # Construct a response with the military units as content
    response_content = "\n".join(military_units)
    response = HttpResponse(response_content, content_type="text/plain")

    return response

