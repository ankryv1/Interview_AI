from fastapi import APIRouter
from app.schemas.user_schema import NewUserSignup
from app.services.auth_service import create_user_service

router = APIRouter(
    prefix="/auth",
    tags=['Authentication']
)

@router.get("/login")
def login():
    return {
        "message": 'this is  login page'
    }

@router.post("/signup")
def signup(user: NewUserSignup):
    return create_user_service(user);
