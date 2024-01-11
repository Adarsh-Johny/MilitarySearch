from SPARQLWrapper import SPARQLWrapper, JSON
from MilitaryDefenseApp.search.query_mappings import QUERY_MAP

import logging

logger = logging.getLogger(__name__)

def execute_search(search_term):
    query_type = ''

    if 'abstract' in search_term: #Usa related queries
        query_type = 'abstract'
    elif 'age range' in search_term:
        query_type = 'ageRange'
    elif 'founding date' in search_term:
        query_type = 'foundingDate'
    elif 'chief minister' in search_term:
        query_type = 'chiefMinister'
    elif 'commander' in search_term:
        query_type = 'commander'
    elif 'chief of command' in search_term:
        query_type = 'commanderInChief'
    elif 'minister' in search_term:
        query_type = 'minister'
    elif 'name' in search_term:
        query_type = 'name'
    elif 'chief of staff' in search_term and 'description' in search_term:
        query_type = 'chief_of_staff_usarmy'

    if query_type in QUERY_MAP:
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setReturnFormat(JSON)
        sparql_query = QUERY_MAP[query_type]
        sparql.setQuery(sparql_query)
        results = sparql.query().convert()

        if results:
            return results
        else:
            return {'message': 'No information found.'}
    else:
        return {'message': 'Please specify your query more clearly. For example: "Who is the commander of the US Army?"'}
