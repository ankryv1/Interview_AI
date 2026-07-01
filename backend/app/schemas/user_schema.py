from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import  Optional


class NewUserSignup(BaseModel):
    """" Schema for validating user cretion of account """
    username: str= Field(..., description='Username of user',min_length=2 )
    email: EmailStr= Field(..., description="Email of user")
    password: str= Field(..., description="User password", min_length=4)

class UserResponse(BaseModel):
    """Schema for data returned to the client """
    id:Optional[str] = None
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
    

