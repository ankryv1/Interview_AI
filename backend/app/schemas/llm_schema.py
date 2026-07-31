from pydantic import BaseModel,Field

#   This contains all AI output schemas

class EvaluationResult(BaseModel):
    score: int= Field(description="Score out of 10")
    feedback: str
    improvement: str
    follow_up_required: bool


class ReportSchema(BaseModel):
    overall_summary: str = Field(description="Overall Performance Summary")
    improvements: list[str] = Field(description="Areas where candidates should improve")
    feedback: str = Field(description="General Feedback")
    technical_feedback: str = Field(description="Technical evaluation")
    communication_feedback: str = Field(description="Communication evaluation")
    strengths: list[str] = Field(description="Strengths of candidate")
    overall_rating: int = Field(ge=0,le=100 ,description="Score out of 100")
