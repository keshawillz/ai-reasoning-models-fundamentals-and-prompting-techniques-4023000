import os
from openai import OpenAI

_ = load_dotenv(find_dotenv()) 

# retrieve OpenAI API key
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY']  
)

response = client.responses.create(
    input="Provide steps I can take to reduce stress during the work",
    model="o4-mini",
    reasoning={
        "effort": "high",  # Can also be "low" or "medium"
        "summary": "auto" # Optional: set to 'auto' to include a summary of the reasoning
    }
)

print(response.output_text)