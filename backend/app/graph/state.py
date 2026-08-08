from typing import List, Optional
from typing_extensions import TypedDict

from app.schemas.interview_schema import InterviewStage, InterviewTurn


class InterviewState(TypedDict):
    # ==============================
    # Interview Configuration
    # ==============================
    user_id: str
    session_id: str
    resume_id: str

    role: str
    difficulty: str
    interview_type: str
    total_questions: int

    # Resume Context (RAG)
    resume_context: str

    # ==============================
    # Current Interview Progress
    # ==============================
    current_question: int
    completed: bool
    state: InterviewStage

    # ==============================
    # Current Turn
    # ==============================
    current_question_text: str
    user_answer: Optional[str]


    # ==============================
    # Conversation History
    # ==============================
    conversation: List[InterviewTurn]

    # ==============================
    # Evaluation
    # ==============================
   
   
    final_report: Optional[str]


#   I used stage here only, as service would get stage from the DB and will pass in the node
# nodes will be independent of the DB,and after node finishes the updated status is written back to the database   