from beanie import Document
from pydantic import Field
from datetime import datetime

class Resume(Document):
    user_id: str | None = None
    filename: str
    extracted_text: str | None = None
    original_filename: str
    file_path: str
    processed: bool = False
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)


class Settings:
    name = "resumes"