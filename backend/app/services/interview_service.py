from fastapi import Depends,HTTPException
from app.utils.dependencies import get_current_user
from app.utils.vector_helpers import get_resume_context
from app.prompts.interview_question_prompt import interview_question_prompt
from app.prompts.evaluation_prompt import evaluation_prompt
from app.rag.llm import llm
from app.models.interview_model import InterviewSession
from app.schemas.interview_schema import StartInterviewRequest
from app.schemas.interview_schema import InterviewTurn
from app.schemas.llm_schema import EvaluationResult

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
    print(response)
    first_turn = InterviewTurn(
        question_number=1,
        topic="unknown",
        question=response.content
    )
    session = InterviewSession(
        user_id = str(current_user.id),
        resume_id = data.resume_id,
        role= data.role,
        difficulty= data.difficuilty,
        interview_type= data.interview_type,
        total_questions= data.total_questions,
        current_question=1,
        conversation = [first_turn]

    )

    await session.insert()
    return {"session_id":str(session.id),
            "answer": response.content}

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
        raise HTTPException(status_code=404, detail="Interview session not found")

    current_turn = session.conversation[-1]
    current_turn.answer = data.answer
    prompt = evaluation_prompt.format_messages(question= current_turn.question, answer=current_turn.answer)

    structured_llm = llm.with_structured_output(EvaluationResult)
    result = structured_llm.invoke(prompt);
    print(result)
    current_turn.score = result.score
    current_turn.feedback = result.feedback
    current_turn.improvement = result.improvement
    current_turn.follow_up = result.follow_up_required

    await session.save()
    return {"answer": result}
