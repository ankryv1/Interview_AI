from dotenv import load_dotenv
import os

load_dotenv()      #  helps  to read .env file

APP_NAME = os.getenv("APP_NAME")        #  helps to read variable from .env
APP_VERSION = os.getenv("APP_VERSION")
MONGODB_URL=os.getenv("MONGODB_URL")
print(MONGODB_URL)
