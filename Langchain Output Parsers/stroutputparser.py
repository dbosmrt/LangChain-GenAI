from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)
#1s prompt -> Detailed report
template1 = PromptTemplate(
    template = "write a detailed report on {topic}",
    input_variables = {'topic'}
)
#2nd prompt -> summary
template = PromptTemplate(
    template = "write a 5 line summary on the following text. /n {text}",
    input_variables = {'text'}

)

parsor = StrOutputParser()
chain = template1 | model | parsor | template | model | parsor

result = chain.invoke({'topic': 'black hole'})

