from app.rag.vector_store import vector_store
from app.rag.llm import llm
from app.prompts.resume_analysis_prompt import resume_analysis_prompt
from app.utils.vector_helpers import get_resume_context

async def analyse_resume_service(resume_id: str):
  context = get_resume_context(resume_id, "Analyse the complete resume",5)
  
  prompt = resume_analysis_prompt.format_messages(context=context)

  response = llm.invoke(prompt)

  return {"analysis": response.content}

