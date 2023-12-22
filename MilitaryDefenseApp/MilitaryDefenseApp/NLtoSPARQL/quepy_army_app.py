from quepy import install
install()

from quepy.dsl import Fixed, HasKeyword, IsRelatedTo, Synset
from quepy.parsing import QuestionTemplate, Particle, Lemma, Pos
from quepy.tagger import get_tagger
from quepy.rdfutils import get_first

# Set the tagger
quepy.set_tagger(get_tagger(False))

# Define Quepy app
class MilitaryCamp(Fixed):
    fixed = "military camp"

class LocationOfMilitaryCamp(QuestionTemplate):
    "Where is X located?"
    regex = (Lemma("where") + Lemma("be") + MilitaryCamp() + Lemma("located") +
             Question(Pos(".")))

    def interpret(self, match):
        camp_name = get_first(match.tokens[2])
        return "SELECT ?location WHERE { ?city dbpedia-owl:location ?location. " \
               f'?city rdfs:label "{camp_name}"@en. }'

class NumOfSoldiers(QuestionTemplate):
    "What is the number of soldiers of X?"
    regex = (Lemma("what") + Lemma("be") + Pos("DT") + Lemma("number") + Pos("IN") + Lemma("soldier") 
             Pos("IN") + MilitaryCamp() + Question(Pos(".")))

    def interpret(self, match):
        camp_name = get_first(match.tokens[5])
        return "SELECT ?population WHERE { ?city dbpedia-owl:populationTotal ?population. " \
               f'?city rdfs:label "{camp_name}"@en. }'

class CommanderOfCamp(QuestionTemplate):
    "Who is the commander of X?"
    regex = (Lemma("who") + Lemma("be") + Pos("DT") + Lemma("commander") +
             Pos("IN") + MilitaryCamp() + Question(Pos(".")))

    def interpret(self, match):
        camp_name = get_first(match.tokens[5])
        return "SELECT ?commander WHERE { ?camp dbpprop:commanderName ?commander. " \
               f'?camp rdfs:label "{camp_name}"@en. }'

# Example usage
if __name__ == "__main__":
    # Sample natural language query
    user_query = "Who is the commander of Washington camp?"

    # Parse the natural language query and generate SPARQL query
    parser = get_parser("army_app")
    query, metadata = parser.get_query(user_query)

    print("Generated SPARQL Query:")
    print(query)

