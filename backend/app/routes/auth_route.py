from fastapi import APIRouter, HTTPException, Response, Cookie
from app.schemas.user_schema import NewUserSignup
from app.services.auth_service import create_user_service, login_service
from app.utils.jwt import create_access_token, verify_access_token
from app.schemas.auth_schema import LoginSchema

router = APIRouter(
    prefix="/auth",
    tags=['Authentication']
)


@router.post("/login")
async def login(credentials: LoginSchema, response: Response):
    user = await login_service(credentials)
    token = create_access_token({"user_id": str(user.id),
                                 "email": user.email})
    
    response.set_cookie(key="access_token", value=token, httponly=True, secure=False, samesite="Lax", max_age=86400)
    return {"message": "Login Successful", "user": user}

@router.post("/signup")
async def signup(user: NewUserSignup, response: Response):

    new_user= await create_user_service(user);
    
    token = create_access_token({"user_id": str(new_user.id),
                                 "email": new_user.email})
    response.set_cookie(key="access_token", value=token, httponly=True, secure=False, samesite="Lax", max_age=86400)
    return {"message": "Signup Successful", "user": new_user}

@router.post("/logout")
async def Logout(response:Response):
    response.delete_cookie("access_token")

    return {"message": "Logged Out Successfully"}   

@router.get("/me")
async def me(access_token: str = Cookie(None)):
    print(access_token)
    if not access_token:
        raise HTTPException(status_code=401, detail="Access token missing")
    payload = verify_access_token(access_token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired Token")
    return { "message": "Authenticated", "user": payload }

