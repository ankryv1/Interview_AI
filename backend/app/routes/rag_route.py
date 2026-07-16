from fastapi import APIRouter, Depends
from app.services.rag_service import retrive_resume_context
from app.utils.dependencies import get_current_user
from app.services.rag_service import analyse_resume_service

router = APIRouter( prefix="/rag", tags=["RAG"])

@router.post("/retriever")
async def retrive_resume_context_route(resume_id: str, question: str, current_user=Depends(get_current_user)):
    answer = await retrive_resume_context(resume_id, question)

    return answer
    
@router.post("/analyse")
async def analyse_resume_route(resume_id:str, current_user=Depends(get_current_user)):
    answer = await analyse_resume_service(resume_id)

    return answer