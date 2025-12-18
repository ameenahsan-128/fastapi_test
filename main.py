from fastapi import FastAPI, Depends
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

# MongoDB configuration
MONGODB_URL = "mongodb://localhost:27017"
DB_NAME = "users"

client = MongoClient(MONGODB_URL)
db = client[DB_NAME]


# Dependency
def get_db():
    return db


# Pydantic model
class Profile(BaseModel):
    name: str
    email: str
    message: str


@app.post("/")
def insert_user(user: Profile, db=Depends(get_db)):
    result = db.users.insert_one(user.dict())
    inserted_user = db.users.find_one({"_id": result.inserted_id})

    # Convert ObjectId to string for JSON serialization
    inserted_user["_id"] = str(inserted_user["_id"])

    return inserted_user
