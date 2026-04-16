from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model = 'gpt-3.5-tubo-instruct')

result = llm.invoke("WHat is the capital of India.")
print(result)



