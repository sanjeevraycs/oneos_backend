from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)

db = client["oneos"]  # DB name

notifications_col = db["notifications"]
emails_col = db["emails"]
users_col = db["users"]
