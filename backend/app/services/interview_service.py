from fastapi import Depends,HTTPException
from app.utils.dependencies import get_current_user
from app.utils.vector_helpers import get_resume_context
from app.prompts.interview_question_prompt import interview_question_prompt
from app.prompts.evaluation_prompt import evaluation_prompt
from app.prompts.followup_prompt import followup_prompt
from app.prompts.next_question_prompt import next_question_prompt
from app.prompts.fiinal_report_prompt import final_report_prompt
from app.rag.llm import llm
from app.models.interview_model import InterviewSession
from app.schemas.interview_schema import StartInterviewRequest, InterviewTurn

from app.schemas.llm_schema import EvaluationResult, ReportSchema

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
    prompt = interview_question_prompt.format_messages(
        context=context, role=data.role, difficulty=data.difficuilty,
        interview_type=data.interview_type, total_questions=data.total_questions
        )

    response = llm.invoke(prompt)
    print(response)
    first_turn = InterviewTurn(
        question_number=1,
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
        conversation = [first_turn],
        resume_context=context
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
        raise HTTPException(status_code=404, detail="Interview Session not found")
    if session.user_id != str(current_user.id):
        raise HTTPException( status_code=401, detail="Unauthorized Request")

    current_turn = session.conversation[-1]
    current_turn.answer = data.answer
    prompt = evaluation_prompt.format_messages(question= current_turn.question, answer=current_turn.answer)

    structured_llm = llm.with_structured_output(EvaluationResult)
    result = await structured_llm.ainvoke(prompt);

    print(result)
    current_turn.score = result.score
    current_turn.feedback = result.feedback
    current_turn.improvement = result.improvement
    current_turn.follow_up = result.follow_up_required

    await session.save()
    if current_turn.follow_up:
        r = await followup_question_service(current_turn.question, current_turn.answer, current_turn.feedback)

        turn = InterviewTurn( question=r, question_number=session.current_question, is_follow_up=True)
        session.conversation.append(turn)
        await session.save()
        return {"type_of": "follow_up", "question": r}
    
    elif session. current_question < session.total_questions:
        r = await next_question_service(session)

        session.current_question+=1
        turn= InterviewTurn(question=r, question_number = session.current_question)
        session.conversation.append(turn)
        await session.save();
        return {"type_of": "next_question", "question": r}
    else:
       report= await generate_report_service(session, current_user)
       session.final_report = report
       await session.save()
       return {"type": "completed", "report": report}
    return {"type": "completed"}

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

async def generate_report_service(session, current_user):

    conversation=""
    for turn in session.conversation:
        conversation+=f"""
        Question: {turn.question}
        Answer: {turn.answer}
        feedback:{ turn.feedback}
        improvement: {turn.improvement}
        Scores: {turn.score}"""
    prompt = final_report_prompt.format_messages(resume_context=session.resume_context, 
                                    conversation=session.conversation,
                                    role=session.role,
                                    difficulty= session.difficulty,
                                    interview_type=session.interview_type,
                                    )
    structured_llm =  llm.with_structured_output(ReportSchema)
    report = await structured_llm.ainvoke(prompt)
    return {"report": report}
