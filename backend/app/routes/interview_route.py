from fastapi import APIRouter,Depends
from app.services.interview_service import start_interview_service
from app.schemas.interview_schema import StartInterviewRequest
from app.utils.dependencies import get_current_user   

router = APIRouter(
    prefix="interview",
    tags=["interview"]
)

@router.post("/start")
async def start_interview(data: StartInterviewRequest, current_user: Depends(get_current_user)):
    await start_interview_service(data, current_user)