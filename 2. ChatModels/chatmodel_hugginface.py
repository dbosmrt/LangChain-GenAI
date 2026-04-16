from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id= 'TinyLlama/TinyLlama-1.1B-Chat-v0.2-GGUF',
    task = "text-generation"
)
model = ChatHuggingFace(llm= llm)

result = model.invoke("what is the capital of India")

print(result.content)
