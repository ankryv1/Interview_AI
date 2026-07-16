from fastapi import Cookie, HTTPException, status
from app.utils.jwt import verify_access_token
from app.models.user_model import User

async def get_current_user(access_token: str = Cookie(None)):
    if access_token is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Not authenticated")
    
    payload = verify_access_token(access_token)
    user = await User.get(payload["user_id"])
    if user is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid or expired Token")
    
    return user  
