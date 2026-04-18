"""
This Lambda is used to convert the python function into a runnalbe.

RunnableLambda is a runnable primitive that allows you to applly custom python functions
with AI pipeline.

It acts as a middleware between different AI components, enabling preprocessing, transformation,
API calls, filtering, and post-processing in a LangChain workfolow.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.shema.runnable import RunnableParallel, RunnableSequence, RunnableLambda, RunnablePassthrough


load_dotenv()

def word_count(text):
    return len(text.split())


prompt = PromptTemplate(
    template= "Write a joke about {topic}",
    input_variables= ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'word_count': RunnableLambda(word_count)
    }
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic': 'AI'})

final_result = """{} \n word count - {}""".format(result['joke'])