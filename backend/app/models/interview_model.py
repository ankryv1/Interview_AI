from beanie import Document
from datetime import datetime
from pydantic import Field
from app.schemas.interview_schema import InterviewTurn   

class InterviewSession(Document):
    user_id: str
    resume_id: str

    role:str
    difficulty: str
    interview_type: str

    total_questions: int
    current_question: int = 0

    conversation: list[InterviewTurn] = Field(default_factory=list)

    scores: list = Field(default_factory=list)
    created_at: datetime = Field(default_factory= datetime.utcnow)
    completed: bool= False

    class Settings:
        name = "interview_sessions"