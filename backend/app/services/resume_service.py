from fastapi import UploadFile
import os
from app.models.resume_model import Resume
import uuid
from app.utils.pdf import extract_text_from_pdf

UPLOAD_DIR = "uploads/resumes"

os.makedirs(UPLOAD_DIR, exist_ok=True)

async def upload_resume_service(file: UploadFile):

    file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_{file.filename}")
    
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    extracted_text = extract_text_from_pdf(file_path)
    print(f" ExtrACTED TEXT IS HERE {extracted_text}")
    
    resume = Resume(
        filename=file.filename,
        original_filename=file.filename,
        file_path=file_path,
        extracted_text=extracted_text,
        processed = True
    )
    await resume.insert()

    return{
        "resume_id": str(resume.id),
        "message": "Resume uploaded successfully",
    }

#   Explanation 
#       1. The first line creates the folder if it does not exists , so if it exists it does not create ensures that the appln does not crash
#      2. it reads the uploaded file, and wb write in binary mode


