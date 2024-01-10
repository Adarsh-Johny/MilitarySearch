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
    'us_headquarters': """
        SELECT (STRAFTER(STR(?headquarters), "http://dbpedia.org/resource/") AS ?headquarters) (STRAFTER(STR(?location), "http://dbpedia.org/resource/") AS ?location) WHERE {
        dbr:United_States_Armed_Forces dbp:headquarters ?headquarters.
        ?headquarters dbo:location ?location
        } LIMIT 1
    """,
    'Lebanon_crisis': """
        SELECT ?abstract ?causalties ?date WHERE {
        dbr:1958_Lebanon_crisis dbo:abstract ?abstract FILTER (LANG(?abstract) = 'en').
        dbr:1958_Lebanon_crisis dbo:causalties ?causalties.
        dbr:1958_Lebanon_crisis dbp:date ?date .
        }

    """, #Last three queries not working properly
    'us_commandStructure': """ 
        SELECT ?branch ?commandStructure WHERE {
        VALUES ?branch {
        dbr:United_States_Air_Force
        dbr:United_States_Army
        dbr:United_States_Coast_Guard
        dbr:United_States_Marine_Corps
        dbr:United_States_Navy
        dbr:United_States_Space_Force
        }

        ?branch dbo:commandStructure ?commandStructure.
        }

    """,
    'American_Civil_War': """
        SELECT DISTINCT ?abstract ?date ?causalties ?results
        WHERE {
        dbr:American_Civil_War dbo:abstract ?abstract FILTER (LANG(?abstract) = 'en').
        OPTIONAL { dbr:American_Civil_War dbo:date ?date }.
        OPTIONAL { dbr:American_Civil_War dbo:causalties ?causalties }.
        OPTIONAL { dbr:American_Civil_War dbo:result ?results }.
        }

    """,
    'War_of_1812': """
        SELECT DISTINCT ?abstract ?date ?causalties ?results WHERE {
        dbr:War_of_1812 dbo:abstract ?abstract FILTER (LANG(?abstract) = 'en').
        OPTIONAL { dbr:War_of_1812 dbo:date ?date }.
        OPTIONAL { dbr:War_of_1812 dbo:causalties ?causalties }.
        OPTIONAL { dbr:War_of_1812 dbo:result ?results }.
        }
    """

}
