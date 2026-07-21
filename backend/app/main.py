from fastapi import FastAPI

from app.routes import resume_route
from app.config import APP_NAME, APP_VERSION
from app.routes import auth_route
from app.routes import rag_route
from app.routes import interview_route
from contextlib import asynccontextmanager
from app.database import init_db
from app.rag.embeddings import embedding_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title=APP_NAME, version=APP_VERSION, lifespan=lifespan)

app.include_router(auth_route.router)

app.include_router(resume_route.router)

app.include_router(rag_route.router)

app.include_router(interview_route.router)



@app.get("/")
def read_root():
    return{
        'message': " hii how are you"
    }


