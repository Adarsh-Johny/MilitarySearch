from django.http import HttpResponse
from SPARQLWrapper import SPARQLWrapper, JSON
from django.shortcuts import render
import logging
import re

logger = logging.getLogger(__name__)


QUERY_MAP = {
    'abstract': """
        SELECT ?abstract WHERE {
            dbr:United_States_Armed_Forces dbo:abstract ?abstract FILTER (LANG(?abstract) = 'en')
            }
    """,
    'ageRange': """
        SELECT ?ageNumber WHERE {
        dbr:United_States_Armed_Forces dbo:ageRange ?ageRange.
        BIND(REPLACE(STR(?ageRange), "^^http://www.w3.org/2001/XMLSchema#nonNegativeInteger", "") AS ?ageNumber)
        }
    """,
    'foundingDate': """
        SELECT ?foundingDate WHERE {
            dbr:United_States_Armed_Forces dbo:foundingDate ?foundingDate
            }
    """,
    'chiefMinister': """
        SELECT ?chiefMinister WHERE {
            dbr:United_States_Armed_Forces dbp:chiefMinister ?chiefMinister
            }
    """,
    'commander': """
        SELECT ?commander
        WHERE {
            dbr:United_States_Armed_Forces dbp:commander ?commander.
        }
    """,
    # 'commanderinchief': """
    #     SELECT ?commanderInChief WHERE {
    #         dbr:United_States_Armed_Forces dbp:commanderInChief ?commanderInChief
    #         }
    # """,
    # chief of staff info - is a sub branch
    'chief_of_staff_usarmy': """
        SELECT ?description WHERE {
        dbr:Chief_of_Staff_of_the_United_States_Army rdfs:comment ?description FILTER (LANG(?description) = 'en')
        }
    """,
    
}

def search(request):
    search_term = request.GET.get("query", '').lower().strip()
    query_type = ''
    
    if 'abstract' in search_term:
        query_type = 'abstract'
    elif 'age range' in search_term : # and 'us army' in search_term:
        query_type = 'ageRange'
    elif 'founding date' in search_term : # and 'us army' in search_term:
        query_type = 'foundingDate'
    elif 'chief minister' in search_term : # and 'us army' in search_term:
        query_type = 'chiefMinister'
    elif 'commander' in search_term : # and 'us army' in search_term:
        query_type = 'commander'
    # elif 'commanderinchief' in search_term:
    #     print("da")
    #     query_type = 'commanderinchief'
    
        # chief of staff info - is a sub branch
    elif 'chief of staff' in search_term and 'description' in search_term:
        query_type = 'chief_of_staff_usarmy'
    
    if query_type in QUERY_MAP:
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setReturnFormat(JSON)
        sparql_query = QUERY_MAP[query_type]
        sparql.setQuery(sparql_query)
        results = sparql.query().convert()
        
        if query_type == 'abstract':
            data = [result["abstract"]["value"] for result in results["results"]["bindings"]]
        elif query_type == 'ageRange':
            data = []
            for result in results["results"]["bindings"]:
                age_range_value = result.get("ageNumber", {}).get("value", "")
                match = re.search(r'\d+', age_range_value)
                if match:
                    data.append(match.group(0))
                else:
                    data.append('No age range provided')
        elif query_type == 'foundingDate':
            data = [result["foundingDate"]["value"] for result in results["results"]["bindings"]]
        elif query_type == 'chiefMinister':
            data = [result["chiefMinister"]["value"] for result in results["results"]["bindings"]]
        elif query_type == 'commander':
            data = [result["commander"]["value"] for result in results["results"]["bindings"]]
        # elif query_type == 'commanderinchief':
        #     data = [result["commanderinchief"]["value"] for result in results["results"]["bindings"]]
            # chief of staff info - is a sub branch
        elif query_type == 'chief_of_staff_usarmy':
            data = [result["description"]["value"] for result in results["results"]["bindings"]]
        
        
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
