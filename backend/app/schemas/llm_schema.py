from pydantic import BaseModel,Field

#   This contains all AI output schemas

class EvaluationResult(BaseModel):
    score: int= Field(description="Score out of 10")
    feedback: str
    improvement: str
    follow_up_required: bool


class ReportSchema(BaseModel):
    overall_summary: str = Field(
        description="A concise summary of the candidate's overall interview performance."
    )

    improvements: list[str] = Field(
        description="Specific areas the candidate should improve."
    )

    feedback: str = Field(
        description="General feedback about the candidate's interview performance."
    )

    technical_feedback: str = Field(
        description="Evaluation of the candidate's technical knowledge and problem-solving."
    )

    communication_feedback: str = Field(
        description="Evaluation of the candidate's communication and explanation quality."
    )

    strengths: list[str] = Field(
        description="Specific strengths demonstrated by the candidate."
    )

    overall_rating: int = Field(
        ge=0,
        le=100,
        description="Overall interview score from 0 to 100."
    )