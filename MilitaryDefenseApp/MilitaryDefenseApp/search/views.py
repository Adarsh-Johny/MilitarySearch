from django.http import HttpResponse
from SPARQLWrapper import SPARQLWrapper, JSON
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


QUERY_MAP = {
    'commanders': """
        SELECT ?commander
        WHERE {
            dbr:United_States_Armed_Forces dbp:commander ?commander.
        }
    """,
    'us_army_commander': """
        SELECT ?name ?description WHERE {
            dbr:Chief_of_Staff_of_the_United_States_Army dbp:name ?name .
            OPTIONAL { dbr:Chief_of_Staff_of_the_United_States_Army rdfs:comment ?description FILTER (LANG(?description) = 'en') }
        }
    """,
}

def search(request):
    search_term = request.GET.get("query", '').lower().strip()
    query_type = ''
    
    if 'commander' in search_term and 'us army' in search_term:
        query_type = 'commanders'
    elif 'commander' in search_term and 'us armed forces' in search_term:
        query_type = 'us_army_commander'
    
    if query_type in QUERY_MAP:
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setReturnFormat(JSON)
        sparql_query = QUERY_MAP[query_type]
        sparql.setQuery(sparql_query)
        results = sparql.query().convert()
        
        if query_type == 'us_army_commander':
            data = [result["name"]["value"] for result in results["results"]["bindings"]]
        else:
            data = [result["commander"]["value"] for result in results["results"]["bindings"] if "commander" in result]
        
        if data:
                return render(request, 'search.html', {'data': data})
        else:
            return render(request, 'search.html', {'message': 'No information found.'})
    else:
        return render(request, 'search.html', {'message': 'Please specify your query more clearly. For example: "Who is the commander of the US Army?"'})


# from django.http import HttpResponse, JsonResponse
# from SPARQLWrapper import SPARQLWrapper, JSON
# from ..open_ai import generate_sparql_query  # Import the utility function

# def search(request):
#     # Retrieve the natural language query from the GET parameters
#     user_query = request.GET.get("query")

#     if not user_query:
#         return JsonResponse({"error": "No query provided"}, status=400)

#     try:
#         sparql_query = generate_sparql_query(user_query)
#     except Exception as e:
#         return JsonResponse({"error": f"Failed to generate SPARQL query: {e}"}, status=500)

#     sparql = SPARQLWrapper("http://dbpedia.org/sparql")
#     sparql.setReturnFormat(JSON)

#     sparql.setQuery(sparql_query)
#     try:
#         results = sparql.query().convert()
#     except Exception as e:
#         return JsonResponse({"error": f"Error in executing SPARQL query: {e}"}, status=500)

#     try:
#         extracted_data = []
#         for result in results["results"]["bindings"]:
#             # Here 'some_field' should be replaced with the actual field name from the results
#             extracted_data.append(result["some_field"]["value"])
#     except Exception as e:
#         # Handle any errors that occur during result processing
#         return JsonResponse({"error": f"Error processing query results: {e}"}, status=500)

#     # Return the extracted data as a JSON response
#     return JsonResponse({"data": extracted_data}, status=200)
