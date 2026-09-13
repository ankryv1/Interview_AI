from app.graph.state import InterviewState
from app.schemas.interview_schema import InterviewStage

# def introduction_router(state: InterviewState):

#     if state["stage"] == InterviewStage.INTRODUCTION:
#         return "introduction"
    

#     return "technical"


# def introduction_followup_router(state: InterviewState):

#     if state["followup_required"] and not state["is_introduction_followup"]:

#         return "followup"

#     return "next_question"


def decision_router(state:InterviewState):


    if state["stage"] == InterviewStage.INTRODUCTION:
         
        if state["followup_required"] and not state["is_introduction_followup"]:
            return "introduction_followup"

        return "generate_first_question"

    if state["stage"]== InterviewStage.TECHNICAL:

        last_turn = state["conversation"][-1]

        if state["followup_required"] and last_turn.follow_up_count<1:
            return "generate_technical_followup_question"

        if state["current_question"] >=state["total_questions"]:
            return "generate_final_report"

        return "generate_next_question"
        
    return "generate_final_report"   


# 

# Router job onlyyy is to inspect the current state and decide the next node