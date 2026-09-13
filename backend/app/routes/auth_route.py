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
    print(payload)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired Token")
    return { "message": "Authenticated", "user": payload }



# At this point, React doesn't need to store the JWT.

# Then:

#                     Browser
#                        │
#                        │ has access_token cookie
#                        ▼
#                   AuthContext
#                        │
#                        │ GET /auth/me
#                        ▼
#                     FastAPI
#                        │
#                        ▼
#                  Verify JWT
#                        │
#                        ▼
#                  Return payload
#                        │
#                        ▼
#               setUser(payload.user)
#                        │
#                        ▼
#              isAuthenticated = true

# That's why /me exists.

# 2. What should /me return?

# Your current route:

# @router.get("/me")
# async def me(access_token: str = Cookie(None)):

# is fine for now.

# It returns:

# {
#     "message": "Authenticated",
#     "user": {
#         "user_id": "...",
#         "email": "..."
#     }
# }

# because your login JWT contains:

# {
#     "user_id": str(user.id),
#     "email": user.email
# }

# Notice something important:

# /me doesn't need the password.

# That's exactly what we want.

# 3. When should /me be called?

# When your React application starts.

# For example:

# User opens:

# http://localhost:5173/

# React starts.

# Then:

# AuthProvider mounts
#        ↓
# GET /auth/me
#        ↓
# Does browser have valid cookie?
#        │
#        ├── YES
#        │    ↓
#        │  user found
#        │    ↓
#        │  setUser(...)
#        │
#        └── NO
#             ↓
#           user = null

# So /me is basically:

# "Backend, check whether this browser already has a valid login."

# This is particularly important after a page refresh.

# 4. Why can't we just set user during login?

# You could do:

# Login
#  ↓
# response contains user
#  ↓
# setUser(response.user)

# But there's a problem.

# Suppose the user refreshes the browser:

# F5

# React state disappears.

# Your:

# const [user, setUser] = useState(null);

# goes back to:

# user = null

# But the HTTP-only cookie still exists.

# So React needs a way to ask:

# "Am I still logged in?"

# That's /me.

# Therefore:

# Login

# Used to establish authentication.

# /me

# Used to restore/check authentication state.