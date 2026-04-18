from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.shema.runnable import RunnableParallel, RunnableSequence, RunnablePassthrough

load_dotenv()



prompt1  = PromptTemplate(
    template = 'Generate a Linkedin post about {topic}',
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template= 'Generate a Tweet about {topic}',
    input_variables= ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    'tweet': RunnableSequence(prompt1, model, parser),
    'Linkedin': RunnableSequence(prompt2, model, parser)
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough()
    'explanation': RunnableSequence('prompt2, model, parser')
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke(result.content))


result = parallel_chain.invoke({'topic': 'AI'})

print(result)