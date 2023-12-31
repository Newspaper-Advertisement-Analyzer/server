from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
import os
from flask_bcrypt import Bcrypt
from Database.db_connector import db
from datetime import datetime

bcrypt = Bcrypt()


def add_user(name, email, password, dbName=db):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    try:
        dbName.User.insert_one({
            "Full_Name": name,
            "Email": email,
            "password": hashed_password,
            "Contact_Number": None,
            "User_Name": name,
            "Registration_Date": datetime.now(),
            "Profession": None,
            "Role": "user",
        })
        return True
    except Exception as e:
        print(e)
        return False


def delete_user(email, dbName=db):
    try:
        dbName.User.delete_one({"Email": email})
        return True
    except Exception as e:
        print(e)
        return False


def find_user(email, dbName=db):
    user = dbName.User.find_one({"Email": email})
    return user


def validate_user(email, password, dbName=db):
    user = dbName.User.find_one({"Email": email})
    if user is None:
        return False
    if not bcrypt.check_password_hash(user["password"], password):
        return False
    return True


def countUers(dbName=db):
    count = dbName.User.count_documents({})
    return count

def replace_password(email, new_password, dbName=db):
    hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
    try:
        dbName.User.update_one({"Email": email}, {"$set": {"password": hashed_password}})
        return True
    except Exception as e:
        print(e)
        return False
