from fastapi import APIRouter, File, HTTPException, UploadFile, Depends
from app.services.resume_service import upload_resume_service
from app.utils.dependencies import get_current_user 
from app.services.resume_service import get_all_resume_service

router= APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

#  look at the incoming requese pull out the fiels called file and put that value into the variable file as UploadFile object

@router.post("/upload")
async def upload_resume_route(file: UploadFile = File(...),current_user =Depends(get_current_user)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    ans= await upload_resume_service(file, current_user)
    return ans


#   get all resume of a user
@router.get("/all")
async def get_all_resume(current_user = Depends(get_current_user)):
    resumes = await get_all_resume_service(current_user)
    return resumes
