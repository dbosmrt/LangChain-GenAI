from langgraph.graph import StateGraph, START, END
from typing import TypedDict

#define state
class BMIState(TypedDict):

    weight_kg: float
    height_m: float 
    bmi: float 
    category: str 

def claculate_bmi(state: BMIState) -> BMIState:

    weight = state['weight_kg']
    height = state['height_m']

    bmi = weight/(height**2)

    state['bmi'] = round(bmi, 2)
    return state 
    
def label_bmi(state: BMIState) -> BMIState:
    # write the bmi labels (if-else loop)
    return None


graph = Stategraph(BMIState)

# add nodes to your graph
graph.add_node('Calculate_bmi', claculate_bmi)
graph.add_node('label_bmi', label_bmi)
#add edges to your graph
graph.add_edge(START, 'calculate_bmi')
graph.add_edge('claculate_bmi', 'label_bmi')
graph.add_edge('label_bmi', END)

# compile the graph
workflow = graph.compile()

# exectute the graph
final_state = workflow.invoke({'weight_kg': 80, 'height_m': 1.73})
print(final_state)


#visualize
from IPython.display import Image
Image(workflow.get_graph().draw_mermaid())
