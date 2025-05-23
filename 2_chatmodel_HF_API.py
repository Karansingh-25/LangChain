from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

llm=HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    cache=False,
    temperature=0
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("What is the Capital of India ?")

print(result.content)