from pydantic import BaseModel,Field

#   This contains all AI output schemas

class EvaluationResult(BaseModel):
    score: int= Field(description="Score out of 10")
    feedback: str
    improvement: str
    follow_up_required: bool

