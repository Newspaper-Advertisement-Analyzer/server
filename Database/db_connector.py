from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv('./.env')

username = os.getenv('DBUSERNAME')
password = os.getenv('PASSWORD')

# client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.lemvb4s.mongodb.net/")
client = MongoClient(
    f"mongodb+srv://nadun:nadun2001@cluster0.lemvb4s.mongodb.net/")
db = client.Advizor
