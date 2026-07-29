from pydantic import BaseModel,Field

#   This contains all AI output schemas

class EvaluationResult(BaseModel):
    score: int= Field(description="Score out of 10")
    feedback: str
    improvement: str
    follow_up_required: bool



class ReportSchema(BaseModel):
    overall_summary: str 
    improvements: list[str]
    feedback: str
    technical_feedback: str
    communication_feedback: str
    strengths: list[str]
    overall_rating: int = Field(ge=0,le=100 ,description="Score out of 100")
