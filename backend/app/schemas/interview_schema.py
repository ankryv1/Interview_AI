from pydantic import BaseModel
from typing import Optional

class StartInterviewRequest(BaseModel):
    resume_id: str
    role: str
    difficuilty: str
    interview_type: str
    total_questions: int

# it only contains what data client(frontend) must send while starting the interview

class InterviewTurn(BaseModel):
    question: str
    answer: Optional[str] = None
    feerback: Optional[str] = None
    score: Optional[int] = None
    topic: str
    question_number: int