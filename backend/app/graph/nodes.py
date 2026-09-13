from app.graph.state import InterviewState
from app.utils.vector_helpers import get_resume_context
from app.prompts.interview_question_prompt import interview_question_prompt
from app.prompts.evaluation_prompt import evaluation_prompt
from app.prompts.next_question_prompt import next_question_prompt
from app.prompts.followup_prompt import followup_prompt
from app.prompts.final_report_prompt import final_report_prompt
from app.rag.llm import llm,evaluate_llm,report_llm
from app.schemas.llm_schema import EvaluationResult, ReportSchema
from app.schemas.interview_schema import InterviewTurn, InterviewStage

async def introduction_node(state: InterviewState):
    question=  """
      Hello!
    Welcome to InterviewAI.
    I'm your interviewer today.
    Before we begin, could you please introduce yourself?
    Tell me about yourself, your background, your projects, and the technologies you've worked with.
    """
    curr_qu = 1
    new_turn = InterviewTurn(question=question, question_number=curr_qu)
    conversation = state["conversation"] + [new_turn]
    # print(updated_state)
    return {"conversation": conversation, "current_question": 1}

async def introduction_followup_node(state: InterviewState):

    turn= state["conversation"][-1]
    prompt = followup_prompt.format_messages(question=turn.question, 
                                             answer=turn.answer, feedback=turn.feedback)
    response = await llm.ainvoke(prompt);
    new_turn = InterviewTurn(question= response.content, question_number=1, is_follow_up=True)
    
    updated_conversation = state["conversation"] + [new_turn]
    return {"is_introduction_followup": True, "conversation": updated_conversation }
    

async def generate_first_question_node(state: InterviewState):
    resume_context = state["resume_context"]
    prompt = interview_question_prompt.format_messages(context= resume_context, role= state["role"], difficulty= state["difficulty"], interview_type= state["interview_type"])

    response = await llm.ainvoke(prompt)
    turn = InterviewTurn(question = response.content, question_number=state["current_question"]+1)
    updated_conversation = state["conversation"] + [turn]
    return {"conversation": updated_conversation, "current_question": state["current_question"] + 1,
             "stage": InterviewStage.TECHNICAL}

async def evaluate_answer_node(state: InterviewState):
    last_turn = state["conversation"][-1]
    print("=====PROMPT======")
    
    prompt = evaluation_prompt.format_messages(question=last_turn.question, answer =state["user_answer"])
    # print(prompt)
    structured_llm = evaluate_llm.with_structured_output(EvaluationResult)
    response = await structured_llm.ainvoke(prompt)
    last_turn.feedback = response.feedback
    last_turn.improvement = response.improvement
    last_turn.score = response.score
    last_turn.answer = state["user_answer"]
    followup_required = response.follow_up_required
    return {"followup_required": followup_required, "conversation": state["conversation"]}


# Generate followup TECHNICAL Question

async def generate_technical_followup_node(state: InterviewState):

    last_turn = state["conversation"][-1]

    prompt = followup_prompt.format_messages(question=last_turn.question, 
                                             answer=last_turn.answer, feedback=last_turn.feedback)
    response = await llm.ainvoke(prompt);
    new_turn = InterviewTurn(question= response.content, question_number=state["current_question"],
                              is_follow_up=True, follow_up_count = last_turn.follow_up_count + 1)
    
    updated_conversation = state["conversation"] + [new_turn]
    return {"conversation": updated_conversation }

async def generate_next_question_node(state:InterviewState):

    history = []

    for turn in state["conversation"]:
        history.append(
            f"""
            question: {turn.question},
            answer: {turn.answer}
            """
        )

    conversation = "/n".join(history)

    prompt = next_question_prompt.format_messages(resume_context=state["resume_context"],
                                                  conversation=conversation,
                                                  role=state["role"],
                                                  interview_type=state["interview_type"],
                                                  current_question=state["current_question"])
    response = await llm.ainvoke(prompt)
    new_turn = InterviewTurn(question= response.content, question_number=state["current_question"]+1)
    updated_conversation = state["conversation"] + [new_turn]
    return {"conversation": updated_conversation, "current_question": state["current_question"] + 1}


async def generate_final_report_node(state: InterviewState):
    prompt = final_report_prompt.format_messages(resume_context=state["resume_context"],
                                                 role=state["role"],
                                                 interview_type=state["interview_type"],
                                                 conversation=state["conversation"]
                                                 )

    str_llm = llm.with_structured_output(ReportSchema)
    response = await str_llm.ainvoke(prompt)
    return {"final_report": response, "completed": True, "state": InterviewStage.COMPLETED, "stage": InterviewStage.COMPLETED}




#  The Flow

# Introduction          6a9db22d8a02f8b2e637f5b6
#       ↓
# Introduction Follow-up (optional)
#       ↓
# First Technical Question
#       ↓
# Technical Follow-up (optional)
#       ↓
# Next Technical Questions
#       ↓
# Final Report
#       ↓
# Interview Completed