from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.models.user_model import User
from app.models.resume_model import Resume
from app.models.interview_model import InterviewSession
from app.config import MONGODB_URL

client = AsyncIOMotorClient(MONGODB_URL)

db = client["interview_ai"]

async def init_db():
    await init_beanie(database=db, document_models=[User,Resume,InterviewSession])
        
