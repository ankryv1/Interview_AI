from langgraph.graph import StateGraph, START, END

from app.graph.nodes import introduction_node
from app.graph.state import InterviewState

graph_builder = StateGraph(InterviewState)

graph_builder.add_node("introduction", introduction_node)

graph_builder.add_edge(START, "introduction")

graph_builder.add_edge("introduction", END)

start_interview_graph = graph_builder.compile()

# Start at START and keep executing nodes until END(simply says start driving)
# await start_interview_graph.ainvoke(state)