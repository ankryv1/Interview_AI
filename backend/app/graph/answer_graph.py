from app.graph.state import InterviewState
from langgraph.graph import StateGraph, START, END

from app.graph.nodes import evaluate_answer_node

evaluate_graph_builder = StateGraph(InterviewState)

evaluate_graph_builder.add_node("evaluate_answer_node", evaluate_answer_node)

evaluate_graph_builder.add_edge(START, "evaluate_answer_node")
evaluate_graph_builder.add_edge("evaluate_answer_node", END)

answer_interview_graph = evaluate_graph_builder.compile()



#                 START
#                   │
#                   ▼
#         evaluate_answer_node
#                   │
#                   ▼
#       is_introduction_router
#           /              \
#         Yes              No
#          │                │
#          ▼                ▼
# generate_first_q      followup_router
#          │                │
#          ▼                │
#         END          ┌────┴────┐
#                      ▼         ▼
#                followup    next_question
#                                 │
#                                 ▼
#                              report?
#                             /      \
#                           Yes      No
#                            │        │
#                            ▼        ▼
#                         report     END