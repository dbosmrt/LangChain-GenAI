from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document

#create Langchain documents for IPL Players

doc1 = Document(
    page_coentent = '',
    metadata = {}
)

doc2 = Document(
    page_coentent = '',
    metadata = {}
)

doc3 = Document(
    page_coentent = '',
    metadata = {}
)

doc4 = Document(
    page_coentent = '',
    metadata = {}
)


docs = [doc1, doc2, doc3, doc4]

vector_store = Chroma(
    embedding_function = OpenAIEmbeddings(),
    persist_directory = 'my-chroma-db',
    collection_name = 'sample'
)

vector_store.add_documents(docs)


vector_store.similarity_search(
    query = 'Who among these are a bowler',
    k=1,
)

vector_sotre.similarity_search_with_score(
    query = "who among these are a bowler",
    k=3
)

# to delete 
vector_store.delete('id which you want to delete.')

