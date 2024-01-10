from SPARQLWrapper import SPARQLWrapper, JSON
from query_mappings import QUERY_MAP

import logging

logger = logging.getLogger(__name__)

def execute_search(search_term):
    query_type = ''

    if 'abstract' in search_term and 'usa armed forces' in search_term: #Usa related queries
        query_type = 'abstract'
    elif 'age range' in search_term and 'usa armed forces' in search_term:
        query_type = 'ageRange'
    elif 'founding date' in search_term and 'usa armed forces' in search_term:
        query_type = 'foundingDate'
    elif 'chief minister' in search_term and 'usa armed forces' in search_term:
        query_type = 'chiefMinister'
    elif 'commander' in search_term and 'usa armed forces' in search_term:
        query_type = 'commander'
    elif 'chief of command' in search_term and 'usa armed forces' in search_term:
        query_type = 'commanderInChief'
    elif 'minister' in search_term and 'usa armed forces' in search_term:
        query_type = 'minister'
    elif 'name' in search_term and 'usa armed forces' in search_term:
        query_type = 'name'
    elif 'chief of staff' in search_term and 'description' in search_term and 'usa armed forces' in search_term:
        query_type = 'chief_of_staff_usarmy'
    elif 'abstract' in search_term and 'british armed forces' in search_term: #Britain related queries
        query_type = 'br_abstract'
    elif 'military size' in search_term and 'british armed forces' in search_term:
        query_type = 'br_militarySize'
    elif 'commander' in search_term and 'british armed forces' in search_term:
        query_type = 'br_commander'
    elif 'start date' in search_term and 'british armed forces' in search_term:
        query_type = 'br_startDate'
    elif 'abstract' in search_term and 'italian armed forces' in search_term: #Italy related queries
        query_type = 'it_abstract'
    elif 'founding date' in search_term and 'italian armed forces' in search_term:
        query_type = 'it_foundingDate'
    elif 'commander' in search_term and 'italian armed forces' in search_term:
        query_type = 'it_commander'
    elif 'chief minister' in search_term and 'italian armed forces' in search_term:
        query_type = 'it_chiefMinister'
    elif 'commander in chief' in search_term and 'italian armed forces' in search_term:
        query_type = 'it_commanderInChief'
    elif 'structure' in search_term and 'italian armed forces' in search_term:
        query_type = 'it_commandStructure'
    elif 'military size' in search_term and 'indian armed forces' in search_term: #India related queries
        query_type = 'ind_militaryUnitSize'
    elif 'commander' in search_term and 'indian armed forces' in search_term:
        query_type = 'ind_commander'
    elif 'Russian Civil War' in search_term and 'result' in search_term: #Battles and operations queries
        query_type = 'Russian_Civil_War'
    elif 'Vietnam War' in search_term and 'description' in search_term:
        query_type = 'Vietnam_War_abstract'
    elif 'Cold War' in search_term and 'description' in search_term:
        query_type = 'Cold_War_comment'
    
    

    if query_type in QUERY_MAP:
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setReturnFormat(JSON)
        sparql_query = QUERY_MAP[query_type]
        sparql.setQuery(sparql_query)
        results = sparql.query().convert()

        # if query_type == 'abstract':
        #     data = [result["abstract"]["value"] for result in results["results"]["bindings"]]
        # elif query_type == 'ageRange':
        #     data = []
        #     for result in results["results"]["bindings"]:
        #         age_range_value = result.get("ageNumber", {}).get("value", "")
        #         match = re.search(r'\d+', age_range_value)
        #         if match:
        #             data.append(match.group(0))
        #         else:
        #             data.append('No age range provided')
        # elif query_type == 'foundingDate':
        #     data = [result["foundingDate"]["value"] for result in results["results"]["bindings"]]
        # elif query_type == 'chiefMinister':
        #     data = [result["chiefMinister"]["value"] for result in results["results"]["bindings"]]
        # elif query_type == 'commander':
        #     data = [result["commander"]["value"] for result in results["results"]["bindings"]]
        # elif query_type == 'commanderInChief':
        #     data = [
        #         result["commanderInChief"]["value"]
        #         for result in results.get("results", {}).get("bindings", [])
        #         if "commanderInChief" in result
        #     ]
        # elif query_type == 'minister':
        #     data = [result["minister"]["value"] for result in results["results"]["bindings"]]
        # elif query_type == 'name':
        #     data = [result["name"]["value"] for result in results["results"]["bindings"]]
        # elif query_type == 'chief_of_staff_usarmy':
        #     data = [result["description"]["value"] for result in results["results"]["bindings"]]

        if results:
            return results
        else:
            return {'message': 'No information found.'}
    else:
        return {'message': 'Please specify your query more clearly. For example: "Who is the commander of the US Army?"'}
