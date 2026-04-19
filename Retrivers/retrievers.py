"""
A retriver is a component in LangChain that fetches relevant documents from a data source in response to a user's query.

There are multiple types of retrievers

All retirevers in LangChain are runnables.
"""

"""
Types of Retrievers - there are a lot of retievers.. you can just look upto to the doucmentation.

Ex. WikiPedia Retrivers.
"""

from langchain_community.retrievers import WikipediaRetriever
from langchain_openai import OpenAIEmbeddings
from langchain.vector_stores import Chroma
retiever = WikipediaRetriever(top_k_results= 2, lang = 'en')

query = 'the geopolitical history in India and Pakistan from perspective of a chinese.'

docs = retiever.invoke(query)

for i, doc in enumerate(docs):
    print(f"\n -- Result {i+1} ----")
    print(f"Content: \n {doc.page_content} -----") # truncate for display

"""
Vector Store Retiever

A vector sotre retiever in LangChain is the most common type of retiever that lets you m
search and fetch documents from a vector store based on semantic similarity using vector embeddings.
"""

documents = [
    #Put all of your documents here
]

embedding_model = OpenAIEmbeddings()

Vectorstore = Chroma.from_documets(
    documents = documents,
    embedding = embedding_model,
    collection_name = 'my_collection'
)

retriever = Vectorstore.as_retriever(search_kwargs=["k":2])

quety = "what is Chroma used for?"

results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(results)

