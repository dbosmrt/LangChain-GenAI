""""
RunnableBranch is a control flow component in LangChain that allow you to conditionally
route input data to different chains or runnalbes based on custom logic.

It funcitons like it/elif/else block for chains - where you define a set of condition functions,
each associated with a runnable(e.g., LLM call, prompt chain, or tool). The first matching
condition is executed. if no condition matches, a default runnable is used(if provided).
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from langchain.schema.runnable import RunnablePassthrough, RunnableBranch, RunnableLambda

load_dotenv()

prompt1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    tmeplate = "summarize the following text \n {text}",
    input_variables= ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({'topic': 'Russia vs Ukraine'})

