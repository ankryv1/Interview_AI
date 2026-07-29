from beanie import Document
from datetime import datetime
from pydantic import Field
from app.schemas.interview_schema import InterviewTurn 
from app.schemas.llm_schema import ReportSchema  

class InterviewSession(Document):
    user_id: str
    resume_id: str
    resume_context: str
    role:str
    difficulty: str
    interview_type: str

    total_questions: int
    current_question: int = 1

    conversation: list[InterviewTurn] = Field(default_factory=list)

    created_at: datetime = Field(default_factory= datetime.utcnow)
    completed: bool= False
    final_report: ReportSchema | None = None
    class Settings:
        name = "interview_sessions"