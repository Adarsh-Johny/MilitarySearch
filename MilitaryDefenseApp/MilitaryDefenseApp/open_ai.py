import openai

def generate_sparql_query(user_query):
    openai.api_key = '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'  # Replace with your actual API key

    response = openai.Completion.create(
      engine="davinci",  # or another appropriate engine
      prompt=user_query,  # the user's natural language input
      max_tokens=150  # adjust based on how long you expect the output to be
    )

    # Extracting the text from the response
    sparql_query = response.choices[0].text.strip()

    return sparql_query
