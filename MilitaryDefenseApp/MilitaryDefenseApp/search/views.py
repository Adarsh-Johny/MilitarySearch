# from django.http import HttpResponse
# from django.shortcuts import render
# from SPARQLWrapper import SPARQLWrapper, JSON
# from .openai_utils import generate_sparql_query  # Import the utility function


# def search(request):
#     # Specify the DBpedia endpoint
#     sparql = SPARQLWrapper("http://dbpedia.org/sparql")
#     sparql.setReturnFormat(JSON)

#     # Define your SPARQL query to retrieve military information
#     query = """
#         SELECT ?commander
#         WHERE {
#             dbr:United_States_Armed_Forces dbp:commander ?commander.
#         }
#     """

#     # Set the SPARQL query and execute it
#     sparql.setQuery(query)
#     results = sparql.query().convert()

#     # Extract relevant information from the query results
#     commanders = [result["commander"]["value"] for result in results["results"]["bindings"]]

#     # Construct a response with the military units as content
#     response_content = "\n".join(commanders)
#     response = HttpResponse(response_content, content_type="text/plain")

#     return response

from django.http import HttpResponse, JsonResponse
from SPARQLWrapper import SPARQLWrapper, JSON
from ..open_ai import generate_sparql_query  # Import the utility function

def search(request):
    # Retrieve the natural language query from the GET parameters
    user_query = request.GET.get("query")

    # If the query parameter is not provided, return an error
    if not user_query:
        return JsonResponse({"error": "No query provided"}, status=400)

    try:
        # Use OpenAI to convert the natural language query to a SPARQL query
        sparql_query = generate_sparql_query(user_query)
    except Exception as e:
        # Handle errors from the OpenAI API call
        return JsonResponse({"error": f"Failed to generate SPARQL query: {e}"}, status=500)

    # Configure the SPARQL endpoint and the return format
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    # Set and execute the generated SPARQL query
    sparql.setQuery(sparql_query)
    try:
        results = sparql.query().convert()
    except Exception as e:
        # Handle errors from the SPARQL query execution
        return JsonResponse({"error": f"Error in executing SPARQL query: {e}"}, status=500)

    # Process the results to extract the necessary data
    try:
        extracted_data = []
        for result in results["results"]["bindings"]:
            # Here 'some_field' should be replaced with the actual field name from the results
            extracted_data.append(result["some_field"]["value"])
    except Exception as e:
        # Handle any errors that occur during result processing
        return JsonResponse({"error": f"Error processing query results: {e}"}, status=500)

    # Return the extracted data as a JSON response
    return JsonResponse({"data": extracted_data}, status=200)
