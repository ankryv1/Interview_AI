from fastapi import APIRouter,Depends
from app.services.interview_service import start_interview_service, answer_interview_service
from app.schemas.interview_schema import StartInterviewRequest, AnswerInterviewRequest
from app.utils.dependencies import get_current_user   

router = APIRouter(
    prefix="/interview",
    tags=["interview"]
)
         
@router.post("/start")
async def start_interview(data: StartInterviewRequest, current_user= Depends(get_current_user)):
   return await start_interview_service(data, current_user)

@router.post("/answer")
async def answer_intereview(data: AnswerInterviewRequest, current_user= Depends(get_current_user)):
   return await answer_interview_service(data, current_user)
                  

#  data is supposed to be StartInterviewRequest object and then uses pydantic to validate the incoming JSON,which is coming from 
# frontend, now 

# Frontend
#    |
#    | POST /start
#    | JSON body
#    ↓
# FastAPI
#    |
#    | "data is StartInterviewRequest"
#    ↓
# Pydantic validation
#    |
#    ├── Valid? ────────→ Create StartInterviewRequest object
#    |                         |
#    |                         ↓
#    |                  start_interview_service()
#    |
#    └── Invalid? ─────→ 422 Unprocessable Entity