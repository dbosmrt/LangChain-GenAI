import os 
#make sure to get yout key of open AI

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import PromptTemplate


#step 1 - Indexing ( document ingestion )

video_id = "id"
try:
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id,languages=['en'])

    #flatten it to plain text
    transcript = " ".join(chunk['text'] for chunk in transcript_list)
    print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video")


#step2 - Chunking (text splitting)
splitter = RecursiveCharacterSplitter(chunk_size = 1000, chunk_overlap=200)
chunks = splitter.create_documents({transcript})

# Embedding Generation and Storing in Vector Store
embeddings = OpenAIEmbeddings(model= 'text-embedding-3-small')
vector_store = FAISS.from_documents(chunks, embeddings)

#step 2 - Retrival
retriever = vector_store.as_retriever(serach_type = 'Similarity', search_kwargs = ('k': 4))
retriever.invoke('What is Deepmind.')

#Step 3
llm = ChatOpenAI(model = 'gpt-4o-mini', temperature = 0.2)
prompt = PromptTemplate(
    template= '''
You are helpful assistant. 
Answer only from the provided transcript context.
If the context is insufficient, just say you don't know.
{context}
question : {question}
''',
input_variables= ['context', 'question']
)

question = "is the topic of aliens discussed in this video? if yes then what was discussed"
retrived_docs = retriever.invoke(question)

context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

final_prompt= prompt.invoke({'context': context_text, 'question': question})

#step 4 generation
answer = llm.invoke(final_prompt)
print(answer.content)
