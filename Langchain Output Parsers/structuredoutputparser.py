from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,

llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

shema = [
    ResponseSchema(name = 'fact_1', description = 'Fact 1 about the topic'),
    ResponseSchema(name = 'fact_1', description = 'Fact 1 about the topic'),
    ResponseSchema(name = 'fact_1', description = 'Fact 1 about the topic')
]

parser = StructuredOutputParser()

template = PromptTemplate(
    template=,
    input_variables=,
    partial_variables=
)

prompt = template.invoke({'topic': 'black hole'})

result = model.invoke(prompt)

finalresult = parser.parse(result.content)

print(finalresult)

