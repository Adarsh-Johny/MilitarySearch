QUERY_MAP = {
    #US Army
    'us_abstract': """
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
    #British army
    'br_abstract': """
        SELECT ?abstract WHERE {
            dbr:British_Army dbo:abstract ?abstract FILTER (LANG(?abstract) = 'en')
            }
    """,
    #Alternatively use dbp:size
    'br_militarySize': """
        SELECT ?militarySize WHERE {
            dbr:British_Army dbo:militaryUnitSize ?militarySize 
            }
    """,
    'br_commander': """
        SELECT ?commander WHERE {
            dbr:United_States_Armed_Forces dbp:commander ?commander.
        }
    """,
    'br_startDate': """
        SELECT ?startDate WHERE {
            dbr:British_Army dbp:startDate ?startDate  
            }
    """,
    #Italian army
    'it_abstract': """
        SELECT ?commander WHERE {
            dbr:Italian_Armed_Forces dbp:commander ?commander 
            }
    """,
    'it_foundingDate': """
        SELECT ?foundingDate WHERE {
            dbr:Italian_Armed_Forces dbo:foundingDate ?foundingDate   
            }
    """,
    'it_commander': """
        SELECT ?commander WHERE {
            dbr:Italian_Armed_Forces dbp:commander ?commander 
            }
    """,
    'it_chiefMinister': """
        SELECT ?chiefMinister WHERE {
            dbr:Italian_Armed_Forces dbp:chiefMinister ?chiefMinister 
            }
    """,
    'it_commanderInChief': """
        SELECT ?commanderInChief WHERE {
            dbr:Italian_Armed_Forces dbp:commanderInChief ?commanderInChief 
            }
    """,
    'it_commandStructure ': """
        SELECT  (STRAFTER(STR(?branch), "http://dbpedia.org/resource/") AS ?branchLabel) WHERE {
            VALUES ?branch { dbr:Italian_Air_Force dbr:Italian_Army dbr:Italian_Navy }
            ?branch dbo:commandStructure ?commandStructure.
            }
    """,
    #Indian army
    'ind_militaryUnitSize': """
        SELECT ?militaryUnitSize WHERE {
            dbr:Indian_Army dbo:militaryUnitSize ?militaryUnitSize .
            }
            ORDER BY DESC(?militaryUnitSize)
            OFFSET 1
            LIMIT 2
    """,
    'ind_commander': """
        SELECT ?commander WHERE {
            dbr:Indian_Army dbp:commander ?commander.
            }
    """,
    #Battles
    'Russian_Civil_War': """
        SELECT ?result WHERE {
            dbr:Allied_intervention_in_the_Russian_Civil_War dbp:result ?result .
            }
    """,
    'Vietnam_War_abstract': """
        SELECT ?abstract WHERE {
            dbr:Vietnam_War dbo:abstract ?abstract FILTER (LANG(?abstract ) = 'en')
            }
    """,
    'Cold_War_comment': """
        SELECT ?comment WHERE {
            dbr:Cold_War rdfs:comment ?comment FILTER (LANG(?comment ) = 'en')
            }
    """
}
