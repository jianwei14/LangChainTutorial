import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint

# Load environment variables from .env file
load_dotenv()

api_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

# Specify the temperature parameter explicitly, not as part of model_kwargs
llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    temperature=0,  # Specify temperature here
    max_length=64,  # Specify max_length here
    max_new_tokens=250,  # Adjust max_new_tokens to be less than or equal to 250
    huggingfacehub_api_token=api_token
)

prompt = "What are good fitness tips?"
response = llm(prompt)

print(response)
