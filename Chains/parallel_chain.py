from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParellel


load_dotenv()

model1 = ChatOpenAI()

model2 = ChatAnthropic(model_name = 'claude-3') #this is not the real name of clause model

prompt1 = PromptTemplate(
    template = ' Generate short and simple notes from the following text \n {text}',
    input_variables= [
        'text'
    ]
)

prompt2 = PromptTemplate(
    template = 'Generate  5 short question from the provided notes \n {text}',
    input_variables= ['text']
)

prompt3 = PromptTemplate(
    template = " merge the provided notes and quiz into a single document \n notes -> {notes} and {quiz}",
    input_variables= ['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParellel(
    {
        'notes': prompt1 | model1 | parser,
        'quiz' : prompt2 | model2 | parser
    }
)

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
The coefficient estimates for Ordinary Least Squares rely on
 the independence of the features. When features are correlated
   and some columns of the design matrix
have an approximately linear dependence, the design matrix becomes
 close to singular and as a result, the least-squares estimate 
 becomes highly sensitive to random errors in the observed target, 
 producing a large variance. This situation of multicollinearity 
 can arise, for example, when data are collected without an 
 experimental design.
"""


