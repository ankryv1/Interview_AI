import fastapi

from app.schemas.user_schema import NewUserSignup
from app.models.user_model import User
from fastapi import HTTPException

async def create_user_service(user: NewUserSignup):
    
    email= user.email
    isExist= await User.find_one(User.email == user.email)
    if isExist:
        raise HTTPException(status_code=400, detail="User already exists")
    
    new_user = User(username=user.username, email=user.email, password=hashed_password)

    await new_user.insert()

    return { "message": "User Created", "user": new_user }