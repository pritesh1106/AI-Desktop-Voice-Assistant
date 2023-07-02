import os
import openai
from config import apikey

openai.api_key = apikey  # Set the OpenAI API key

# Create an AI completion request
response = openai.Completion.create(
  model="text-davinci-003",  # Specify the language model to use
  prompt="Write an email to my boss for resignation?",  # Provide the prompt for the AI to generate a completion
  temperature=0.7,  # Controls the randomness of the output (higher value = more randomness)
  max_tokens=256,  # Limit the length of the generated completion
  top_p=1,  # Controls the diversity of the output (1.0 means no truncation)
  frequency_penalty=0,  # Adjusts the likelihood of the AI repeating the same response
  presence_penalty=0  # Adjusts the likelihood of the AI including new information
)

print(response)  # Print the response received from the OpenAI API
