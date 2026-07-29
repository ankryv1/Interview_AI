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
    feedback: Optional[str] = None
    improvement: str | None = None
    follow_up: bool = False
    score: Optional[int] = None
    question_number: int
    is_follow_up: bool = False


class AnswerInterviewRequest(BaseModel):
    session_id: str
    answer: str


#    this part contains all API request/response schemas