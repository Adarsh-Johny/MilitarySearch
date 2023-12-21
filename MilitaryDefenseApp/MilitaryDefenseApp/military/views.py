# your_app_name/views.py
from django.http import JsonResponse
import requests

# def military(request):
#     # url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/military-bases/records?limit=20"
#     # url = "https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Property_and_Land_WebMercator/MapServer/11/query?where=1%3D1&outFields=*&outSR=4326&f=json"
#     # url="http://catalog.data.gov/api/3/"
#     url="https://www.de-vis-software.ro/fightcurrus.aspx"
    
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
#         data = response.json()
#         # Process the data as needed
#         # For example, you can extract information from 'data' variable

#         return JsonResponse(data, safe=False)
#     except requests.exceptions.RequestException as e:
#         # Handle exceptions, such as network errors or invalid response
#         return JsonResponse({"error": str(e)}, status=500)

from SPARQLWrapper import SPARQLWrapper, JSON

def military():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)
    query = """
        PREFIX dbres: <http://dbpedia.org/resource/>
        DESCRIBE dbres:United_States
    """
    sparql.setQuery(query)
    return sparql.query().convert()