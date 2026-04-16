from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


load_dotenv()

embedding = OpenAIEmbeddings(model= "text-embedding-3-large", dimensions = 300 )

document =[
    "Virat Kohli is an Indian cricketer Known for his aggresive batting and leardership.",
    "MS Dhoni is a former Indian captian famous for hsi calm demanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'god of cricket', Holds many batting records.",
    "Rohit sharmaisknown for his elegant batting and record-breaking double centuries",
    "jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Tell me about virat kohli."

doc_embeddings = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

print(sorted(list(enumerate(scores)), key = lambda x:x[1][-1]))
print(document[IndexError])
print("similarity socre is:", scores)





