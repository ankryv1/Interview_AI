from typing import List, Optional
from typing_extensions import TypedDict
from app.schemas.llm_schema import EvaluationResult, ReportSchema

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
    followup_required: Optional[bool]
    is_introduction_followup: bool
    user_answer: str

    # Resume Context (RAG)
    resume_context: str

    # ==============================
    # Current Interview Progress
    # ==============================
    current_question: int
    completed: Optional[bool]
    stage: InterviewStage

    # ==============================
    # Current Turn
    # ==============================

    # ==============================
    # Conversation History
    # ==============================
    conversation: List[InterviewTurn]

    # ==============================
    # Evaluation
    # ==============================
    
   
    final_report: Optional[ReportSchema]


#   I used stage here only, as service would get stage from the DB and will pass in the node
# nodes will be independent of the DB,and after node finishes the updated status is written back to the database   