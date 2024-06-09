import os
from langchain_openai.llms import OpenAI
from dotenv import load_dotenv

# Load env variable from .env file
load_dotenv()

# Retrieve the API Key from env variables
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# temperature lies between 0 and 1
# default Open AI models is text-davinci-003
llm = OpenAI(temperature=0.9)
prompt = "What would a good company name be for a company that makes colorful socks?"

print(llm(prompt))
