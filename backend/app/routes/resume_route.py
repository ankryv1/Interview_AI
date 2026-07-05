from fastapi import APIRouter, File, HTTPException, UploadFile
from app.services.resume_service import upload_resume_service

router= APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

#  look at the incoming requese pull out the fiels called file and put that value into the variable file as UploadFile object

@router.post("/upload")
async def upload_resume_route(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    ans= await upload_resume_service(file)
    return ans