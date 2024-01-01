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
}

def search(request):
    query_type = request.GET.get("type", 'commanders')
    
    if query_type not in QUERY_MAP:
        return HttpResponse("Invalid query type", status=400)
    
    search_term = request.GET.get("query", '').strip()
    
    if search_term:
    
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setReturnFormat(JSON)

        sparql.setQuery(QUERY_MAP[query_type])
        results = sparql.query().convert()
        
        data = [result["commander"]["value"] for result in results["results"]["bindings"]]
        
        return render(request, 'search.html', {'data': data, 'query': search_term})
    return render(request, 'search.html', {'message': 'No information found.'})


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
