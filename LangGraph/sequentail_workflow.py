from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI()

class LLMState(TypedDict):
    
    question: str
    answer: str

def llm_qa(state: LLMState) -> LLMState:

    question = state['question']

    prompt = f"Answer the following question {question}"

    answer = model.invoke(prompt).content
    state['answer']  = answer

    reutrn state

# create a graph
graph = StateGraph(LLMState)

graph.add_node('llm_qa', llm_qa)

#add edges
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)
workflow = graph.compile()

inital_state ={'question': 'How far is moon form earth?'}

final_state = workflow.invoke(initial_state)
print(final_state['ansewer'])
