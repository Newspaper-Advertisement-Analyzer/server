from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
load_dotenv('..env')

username: str = os.getenv('DBUSERNAME')
password: str = os.getenv('PASSWORD')

client = MongoClient("mongodb+srv://"+username+":"+password +"@cluster0.lemvb4s.mongodb.net/")
db = client.NewspaperAdAnalyzer

def add_user(name,email,password):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    try:
        db.user.insert_one({"name":name,"email":email,"password":hashed_password})
        return True
    except:
        return False


def find_user(email):
    user = db.user.find_one({"email":email})
    return user

def validate_user(email,password):
    user = db.user.find_one({"email":email})
    if user is None:
        return False
    if not bcrypt.check_password_hash(user["password"], password):
        return False
    return True