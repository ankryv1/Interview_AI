from app.graph.state import InterviewState
from app.utils.vector_helpers import get_resume_context
from app.prompts.interview_question_prompt import interview_question_prompt
from app.prompts.evaluation_prompt import evaluation_prompt
from app.rag.llm import llm
from app.schemas.llm_schema import EvaluationResult, ReportSchema

async def introduction_node(state: InterviewState):
    question=  """
      Hello!

    Welcome to InterviewAI.

    I'm your interviewer today.

    Before we begin, could you please introduce yourself?

    Tell me about yourself, your background, your projects, and the technologies you've worked with.

    """
    curr_qu = 1
    updated_state = {"current_question_text": question, "current_question": curr_qu}
    # print(updated_state)
    return updated_state

async def generate_first_question_node(state: InterviewState):
    resume_context = state["resume_context"]
    prompt = interview_question_prompt.format_messages(context= resume_context, role= state["role"], difficulty= state["difficulty"], interview_type= state["interview_type"])

    response = await llm.ainvoke(prompt)

    return {"current_question_text": response.content, "current_question": 2}

async def evaluate_answer_node(state: InterviewState,):
    last_turn = state["conversation"][-1]
    print("=====PROMPT======")
    
    prompt = evaluation_prompt.format_messages(question=last_turn.question, answer =state["user_answer"])
    print(prompt)
    structured_llm = llm.with_structured_output(EvaluationResult)
    response = await structured_llm.ainvoke(prompt)
    print("=====RESPONSE======")
    print(response)
    return response
