from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
from Database.db_connector import db
from datetime import datetime

bcrypt = Bcrypt()
# load_dotenv('./.env')

# username: str = os.getenv('DBUSERNAME')
# password: str = os.getenv('PASSWORD')

# client = MongoClient("mongodb+srv://"+username+":"+password +"@cluster0.lemvb4s.mongodb.net/")
# db = client.NewspaperAdAnalyzer

def add_user(name, email, password):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    try:
        db.User.insert_one({
            "Full_Name": name,
            "email": email,
            "User_ID": "pu1011",
            "password": hashed_password,
            "Contact_Number": None,
            "User_Name": name,
            "Registration_Date": datetime.now(),
            "Profession": None,
            "Role": "user"
        })
        return True
    except Exception as e:
        print(e)
        return False

def delete_user(email):
    try:
        db.User.delete_one({"email": email})
        return True
    except Exception as e:
        print(e)
        return False

def find_user(email):
    user = db.User.find_one({"email": email})
    return user

def validate_user(email, password):
    user = db.User.find_one({"email": email})
    if user is None:
        return False
    if not bcrypt.check_password_hash(user["password"], password):
        return False
    return True

def countUers():
    count = db.User.count_documents({})
    return count