from datetime import datetime
from beanie import Document
from pydantic import EmailStr, Field
from bson import ObjectId

class User(Document):
   
    username: str
    password: str
    email: EmailStr
    created_at: datetime = Field(default_factory=datetime.now) 
    updated_at: datetime = Field(default_factory=datetime.now)
#   dict bhi ek python document hai jo key value pair me store krta hai values ko 

    class Settings:
        name="users"