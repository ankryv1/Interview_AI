from pydantic import BaseModel

class ResumeOut(BaseModel):
    resume_id: str
    user_id: str
    filename: str
