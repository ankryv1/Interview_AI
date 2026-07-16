from app.rag.vector_store import vector_store
from app.rag.llm import llm
from app.prompts.resume_qa_prompt import resume_qa_prompt
from app.prompts.resume_analysis_prompt import resume_analysis_prompt
from app.utils.vector_helpers import get_resume_context  

async def retrive_resume_context(resume_id:str, question: str):
    retriever = vector_store.as_retriever( search_kwargs ={"k":3, "filter":{"resume_id": resume_id}})

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = resume_qa_prompt.format_messages(context=context,
                                       question=question)
    
    response = llm.invoke(prompt)
    return {"answer": response.content}
 
async def analyse_resume_service(resume_id: str):
  context = get_resume_context(5,resume_id, "Analyse the complete resume")

  prompt = resume_analysis_prompt.format_messages(context=context)

  response = llm.invoke(prompt)

  return {"analysis": response.content}
 