from fastapi import UploadFile
import os
from app.models.resume_model import Resume
import uuid
from app.utils.pdf import extract_text_from_pdf
from app.rag.splitter import text_splitter
from app.rag.vector_store import add_resume_to_vector_store

UPLOAD_DIR = "uploads/resumes"

os.makedirs(UPLOAD_DIR, exist_ok=True)

async def upload_resume_service(file: UploadFile, current_user):

    file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_{file.filename}")
      
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)


    extracted_text = extract_text_from_pdf(file_path)

    text_chunks = text_splitter(extracted_text)
    
    
    print("Text chunks:", text_chunks)
    print("Number of chunks:", len(text_chunks))

    resume = Resume(
        filename=file.filename,
        user_id= str(current_user.id),
        original_filename=file.filename,
        file_path=file_path,
        extracted_text=extracted_text,
        processed = True
    )
    await resume.insert()
    add_resume_to_vector_store(chunks=text_chunks, resume_id=str(resume.id), user_id=str(current_user.id) )
    
    return{
        "resume_id": str(resume.id),
        "message": "Resume uploaded successfully",
    }

#   Explanation 
#       1. The first line creates the folder if it does not exists , so if it exists it does not create ensures that the appln does not crash
#      2. it reads the uploaded file, and wb write in binary mode


