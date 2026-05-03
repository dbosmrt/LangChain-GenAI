from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class BatsmanState(TypedDict):

    runs: int
    balls: int
    fours: int
    sixes: int 


    sr: float 
    bpb: float 
    boundary_percent: float 


graph = StateGraph(BatsmanState)

graph.add_node('calculate_sr', calculate_sr)
graph.add_note('calculate_bpb' calculate_bpb)
graph.add_note('calculate_boundary_percent' calculate_boundary_percent)
graph.add_note('summary' summary)

def calculate_sr (state:BatsmanState):
     bpb = state['balls']/(state['fours']) + state['sixes']
     state['bpb'] = bpb 
     return state 


def calcualte_boundary_percent(state: BatsmanState):
     boundary_percent = state['boundary_percent']


# for parallel workflows
graph.add_edge(START, 'calcualate_sr')
graph.add_edge(START, 'calcualate_bpb')
graph.add_edge(START, 'calcualate_boundary_percent')

graph.add_edge('calculate_sr', 'summary')
graph.add_edge('calculate_sr', 'summary')
graph.add_edge('calculate_sr', 'summary')