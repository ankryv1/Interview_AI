from datetime import datetime, timedelta

from fastapi import HTTPException
import jwt

from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRY_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+ timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str):
     try:
          payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
          return payload
     except jwt.PyJWTError:
          raise HTTPException(status_code=401, detail="Invalid token")