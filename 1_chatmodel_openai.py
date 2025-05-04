from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model=ChatOpenAI(
    model="gpt-4",
    openai_api_key=os.getenv("OPENAI_API")
)

result=model.invoke("What is the capital of India ?")

print(result)


# This Code also Does not Work because the reson is Same