import fastapi

from app.schemas.user_schema import NewUserSignup
from app.models.user_model import User
from fastapi import HTTPException
from app.utils.password import hash_password, verify_password
from app.utils.jwt import create_access_token
from app.schemas.auth_schema import LoginSchema

async def create_user_service(user: NewUserSignup):
    
    isExist= await User.find_one(User.email== user.email)
    if isExist:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, email=user.email, password=hashed_password)

    await new_user.insert()
    token = create_access_token({"user_id": str(new_user.id), "email": new_user.email})

    return new_user

async def login_service(login_data: LoginSchema):
    user_found = await User.find_one(User.email == login_data.email)
    if not user_found:
        raise HTTPException(status_code=404, detail="User not found with this email")
    
    is_valid = verify_password(login_data.password, user_found.password)
    if not is_valid:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return user_found