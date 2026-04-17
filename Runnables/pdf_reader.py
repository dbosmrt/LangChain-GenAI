from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI

#Load the document 
loader = TextLoader('docs.txt') # ensure docs txt exists
documents = loader.load()

# split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap= 50)
docs = text_splitter.split_documents(documents)

# Convert text into embeddings & store in FAISS
vectorestore = FAISS.from_documents(docs, OpenAIEmbeddings())

#Create a retiver (fetches releavant documents)
retriver = vectorestore.as_retriver()

# Manually retrieve relevant documents
query = "What are the key takeaways from the documents?"
retrieved_docs = retriver.get_relevant_documents(query)

#combine retirved text into a single prompt
retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])

#initialize the LLM
llm = OpenAI(model_name= 'gpt-3.5-turbo', temperature = 0.7)

# Manually Pass Retrieved Text to LLM
prompt = f"Based on the following text, answer the question: {query}\n\n{retrieved_text}"
answer = llm.predict(prompt)

# print the answer
print("Answer:", answer)

