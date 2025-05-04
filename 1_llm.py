from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm=OpenAI(model='gpt-3.5-turbo-instruct',
           openai_api_key=os.getenv("OPENAI_API"))

result=llm.invoke("What is the capital of India ?")

print(result)

# This code Gives RateLimit Error Because no credits in OpenAI account