from fastapi import Depends,HTTPException
from app.utils.dependencies import get_current_user
from app.utils.vector_helpers import get_resume_context
from app.prompts.interview_question_prompt import interview_question_prompt
from app.prompts.evaluation_prompt import evaluation_prompt
from app.prompts.followup_prompt import followup_prompt
from app.prompts.next_question_prompt import next_question_prompt
from app.prompts.fiinal_report_prompt import final_report_prompt
from app.rag.llm import llm
from app.rag.llm import report_llm

from app.graph.interview_graph import start_interview_graph
from app.graph.answer_graph import answer_interview_graph
from app.models.interview_model import InterviewSession
from app.schemas.interview_schema import StartInterviewRequest, InterviewTurn, InterviewStage

from app.schemas.llm_schema import ReportSchema


# to ask question regarding the resume
def get_interview_service(question: str, resume_id: str, current_user):
    context = get_resume_context(resume_id,"Get parts from where interview questions can be generated")

    prompt = interview_question_prompt.format_messages(context=context)
    response = llm.invoke(prompt)
    return {"answer": response.content}

async def start_interview_service(data: StartInterviewRequest, current_user):
    context = get_resume_context(
        resume_id= data.resume_id,
        question=f"""Generate interview questions for a {data.role} interview. Focus on projects, skills and experience.""",
        k=8
       )
    # print("Context:", context)

    session = InterviewSession(
        user_id = str(current_user.id),
        resume_id = data.resume_id,
        role= data.role,
        difficulty= data.difficuilty,
        interview_type= data.interview_type,
        total_questions= data.total_questions,
        current_question=1,
        conversation = [],
        stage= InterviewStage.INTRODUCTION,
        resume_context=context
        )

    await session.insert()

    state={
            "user_id": current_user.id,
            "session_id" : str(session.id),
            "resume_id": str(data.resume_id),
            "role": data.role,
            "difficulty": data.difficuilty,
            "interview_type": data.interview_type,
            "conversation": [],
            "resume_context":context,
            "current_question": 1,
            "stage": InterviewStage.INTRODUCTION,
        }
    updated_state = await start_interview_graph.ainvoke(state)
    # prompt = interview_question_prompt.format_messages(
    #     context=context, role=data.role, difficulty=data.difficuilty,
    #     interview_type=data.interview_type, total_questions=data.total_questions
    #     )

    # response = llm.invoke(prompt)
    # print(response)
    # first_turn = InterviewTurn(
    #     question_number=1,
    #     question=response.content
    # )

    session.conversation.append(InterviewTurn(
        question_number=1, question=updated_state["current_question_text"]))
    await session.save()

    return {"session_id":str(session.id),
            "question":updated_state["current_question_text"],
            "question_number":updated_state["current_question"]
            }

# Client
#       │
#       ▼
# POST /interview/start
#       │
#       ▼
# Retrieve Resume Context
#       │
#       ▼
# LLM generates Question 1
#       │
#       ▼
# Create InterviewTurn
#       │
#       ▼
# Create InterviewSession
#       │
#       ▼
# Save to MongoDB
#       │

#       ▼
# Return session_id + question

async def answer_interview_service(data ,current_user):
    session = await InterviewSession.get(data.session_id)

    if not session:
        raise HTTPException(status_code=404, detail="Interview Session not found")
    if session.user_id != str(current_user.id):
        raise HTTPException( status_code=401, detail="Unauthorized Request")

    current_turn = session.conversation[-1]
    current_turn.answer = data.answer
    session.save();
    state= {
        "user_id": current_user.id,
        "session_id" : str(session.id),
        "resume_id": str(session.resume_id),
        "role": session.role,
        "difficulty": session.difficulty,
        "interview_type": session.interview_type,
        "stage": session.stage,
        "current_question": current_turn.question,
        "resume_context": session.resume_context,
        "conversation": session.conversation,
        "user_answer": data.answer
    }
   
    updated_state = await answer_interview_graph.ainvoke(state)
    print("Updated_State:", updated_state)
    return updated_state
    
    
    

async def followup_question_service(question, answer, feedback):
    prompt = followup_prompt.format_messages(question=question, answer=answer, feedback=feedback)

    result = await llm.ainvoke(prompt)
    print(result)

    return result.content

async def next_question_service(session):
    conversation = ""

    for turn in session.conversation:
        conversation+=f"""
        Question: {turn.question}
        Answer: {turn.answer}
        """
    prompt = next_question_prompt.format_messages(
        resume_context=session.resume_context,
        conversation=conversation,
        interview_type=session.interview_type,
        role=session.role,
        difficulty=session.difficulty,
        current_question=session.current_question
    )
    result = await llm.ainvoke(prompt)
    return result.content

async def generate_report_service(session):

    conversation=""
    for turn in session.conversation:
        conversation+=f"""
        Question: {turn.question}
        Answer: {turn.answer}
        feedback:{ turn.feedback}
        improvement: {turn.improvement}
        Scores: {turn.score}"""
    prompt = final_report_prompt.format_messages(resume_context=session.resume_context, 
                                    conversation=conversation,
                                    role=session.role,
                                    difficulty= session.difficulty,
                                    interview_type=session.interview_type,
                                    )
    structured_report_llm =  report_llm.with_structured_output(ReportSchema)
    report = await structured_report_llm.ainvoke(prompt)
    session.completed = True
    return  report
