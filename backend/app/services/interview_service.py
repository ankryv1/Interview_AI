from fastapi import Depends
from app.utils.dependencies import get_current_user
from app.utils.vector_helpers import get_resume_context
from app.prompts.interview_question_prompt import interview_question_prompt
from app.rag.llm import llm
from app.models.interview_model import InterviewSession
from app.schemas.interview_schema import StartInterviewRequest

def get_interview_service(question: str, resume_id: str, current_user: Depends(get_current_user)):
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
    prompt = interview_question_prompt.format_messages(
        context=context, role=data.role, difficulty=data.difficuilty,
        interview_type=data.interview_type, total_questions=data.total_questions
        )

    response = llm.invoke(prompt)
    return {"answer": response.content}