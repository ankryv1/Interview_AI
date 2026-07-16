from dotenv import load_dotenv
import os

load_dotenv()      #  helps  to read .env file

APP_NAME = os.getenv("APP_NAME")        #  helps to read variable from .env
APP_VERSION = os.getenv("APP_VERSION")
MONGODB_URL=os.getenv("MONGODB_URL")
ACCESS_TOKEN_EXPIRY_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRY_MINUTES"))
ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")
GROQ_API_KEY=os.getenv("GROQ_API_KEY")
