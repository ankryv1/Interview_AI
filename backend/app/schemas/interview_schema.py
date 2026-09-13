from pydantic import BaseModel
from typing import Optional
from enum import Enum

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
    follow_up_count: int = 0
    score: Optional[int] = None
    question_number: int
    is_follow_up: bool = False


class AnswerInterviewRequest(BaseModel):
    session_id: str
    answer: str

class InterviewStage(str, Enum):
    INTRODUCTION = "INTRODUCTION"
    TECHNICAL = "TECHNICAL"
    COMPLETED = "COMPLETED"

#    this part contains all API request/response schemas



#    Flow to update current_question

# What happens after Question 3?

# User answers.

# Create

# InterviewTurn(
#     question_number=3,
#     ...
# )

# Append it.

# Now

# conversation = [

# Turn1,

# Turn2,

# Turn3
# ]

# Then update

# current_question += 1

# Now

# current_question = 4