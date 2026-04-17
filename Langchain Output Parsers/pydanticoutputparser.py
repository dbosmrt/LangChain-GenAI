from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
llm = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):

    name : str = Field(description = 'Name of the person')
    age: int = Field (ge=18, description = "Age of the person")
    city : str = Field(description= "Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = "genearate the name, age and city of a ficational {place} person \n {format_instruction}",
    input_variables= ["place"],
    parital_variables = ['format_instruction': parser.get_format_instruction()]
)

prompt = template.invoke ({'Place': 'Indian'})
final_result = parser.parse(prompt)

print(final_result)

#or you can make it easy using chain
chain = template | model | parser

final_result = chain.invoke({
    'place': 'sri lankan'
})

print(final_result)

