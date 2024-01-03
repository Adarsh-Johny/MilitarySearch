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
    'commanderInChief': """
        SELECT ?commanderInChief WHERE {
            dbr:United_States_Armed_Forces dbp:commanderInChief ?commanderInChief
            }
    """,
    'minister': """
        SELECT ?minister
        WHERE {
            dbr:United_States_Armed_Forces dbp:minister ?minister.
        }
    """,
    'name': """
        SELECT ?name
        WHERE {
            dbr:United_States_Armed_Forces dbp:name ?name.
        }
    """,
    'chief_of_staff_usarmy': """
        SELECT ?description WHERE {
        dbr:Chief_of_Staff_of_the_United_States_Army rdfs:comment ?description FILTER (LANG(?description) = 'en')
        }
    """,
}
