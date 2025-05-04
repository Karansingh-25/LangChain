from langchain_ollama import OllamaLLM

llm=OllamaLLM(model="llama3.2",
              temperature=1.9,)
            #   cache=False)

response=llm.invoke("What is Capital of India ?")

print(response)