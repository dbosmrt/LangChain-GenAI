from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.shema.runnable import RunnableSequence

prompt = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables= ['topic']

)

prompt2 = PromptTemplate(
    template = "Expalin the following joke - {text}",
    input_variables= ['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

