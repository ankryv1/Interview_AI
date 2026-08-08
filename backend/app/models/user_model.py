from datetime import datetime
from beanie import Document, Indexed
from typing import Annotated
from pydantic import EmailStr, Field
from bson import ObjectId

class User(Document):
   
    username: Annotated[str,Indexed()]
    password: str
    email: Annotated[EmailStr,Indexed(unique=True)]
    created_at: datetime = Field(default_factory=lambda: datetime.now()) 
    updated_at: datetime = Field(default_factory=lambda: datetime.now())
#   dict bhi ek python document hai jo key value pair me store krta hai values ko 

    class Settings:
        name="users"

#  without lambda some systems get confused with weather its executing a function or passing a factory
#  with lambda it creates a anonymous function wrapper, tells that do not run this fn now, run this everytime the new user instance is created