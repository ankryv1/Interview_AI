from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import  Optional

class LoginSchema(BaseModel):
    """Schema for validating user Login"""
    email: EmailStr= Field(..., description="Email of user")
    password: str = Field(..., description="User Password", min_length=4)