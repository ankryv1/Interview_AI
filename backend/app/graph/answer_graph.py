from app.graph.state import InterviewState
from langgraph.graph import StateGraph, START, END
from app.graph.routers import decision_router

from app.graph.nodes import evaluate_answer_node
from app.graph.nodes import introduction_followup_node
from app.graph.nodes import generate_first_question_node
from app.graph.nodes import generate_technical_followup_node
from app.graph.nodes import generate_next_question_node
from app.graph.nodes import generate_final_report_node

evaluate_graph_builder = StateGraph(InterviewState)

evaluate_graph_builder.add_node("evaluate_answer_node", evaluate_answer_node)

evaluate_graph_builder.add_node("introduction_followup_node", introduction_followup_node)

evaluate_graph_builder.add_node("generate_first_question_node", generate_first_question_node)
evaluate_graph_builder.add_node("generate_technical_followup_node", generate_technical_followup_node)

evaluate_graph_builder.add_node("generate_next_question_node", generate_next_question_node)
evaluate_graph_builder.add_node("generate_final_report_node", generate_final_report_node)

evaluate_graph_builder.add_edge(START, "evaluate_answer_node")

evaluate_graph_builder.add_conditional_edges(
    "evaluate_answer_node", 
    decision_router,
    {
        "introduction_followup": "introduction_followup_node",
        "generate_first_question": "generate_first_question_node",
        "generate_technical_followup_question": "generate_technical_followup_node",
        "generate_next_question": "generate_next_question_node",
        "generate_final_report": "generate_final_report_node"
    }
)

evaluate_graph_builder.add_edge("introduction_followup_node",END)
evaluate_graph_builder.add_edge("generate_first_question_node",END)
evaluate_graph_builder.add_edge("generate_technical_followup_node",END)
evaluate_graph_builder.add_edge("generate_next_question_node",END)
evaluate_graph_builder.add_edge("generate_final_report_node",END)

answer_interview_graph = evaluate_graph_builder.compile()


#                  START
#                    │
#                    ▼
#         evaluate_answer_node
#                    │
#                    ▼
#             decision_router
#       ┌─────────┼──────────┬──────────────┬──────────────┐
#       ▼         ▼          ▼              ▼              ▼
# intro_followup first_q  tech_followup  next_question  final_report
#       │         │          │              │              │
#       └─────────┴──────────┴──────────────┘              │
#                     │                                    │
#                     ▼                                    ▼
#            evaluate_answer_node                         END

#   GRAPH ends after producing one question, because every HTTP Request corresponds to one graph execution.



# evaluate
#      │
#      ▼
# router
#      │
#      ├────────► introduction_followup
#      │                 │
#      │                 ▼
#      │                END
#      │
#      ├────────► generate_first_question
#      │                 │
#      │                 ▼
#      │                END
#      │
#      ├────────► generate_technical_followup
#      │                 │
#      │                 ▼
#      │                END
#      │
#      ├────────► generate_next_question
#      │                 │
#      │                 ▼
#      │                END
#      │
#      └────────► generate_final_report
#                        │
#                        ▼
#                       END