from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
import os
load_dotenv('Database\.env')

username: str = os.getenv('DBUSERNAME')
password: str = os.getenv('PASSWORD')

client = MongoClient("mongodb+srv://"+username+":"+password +"@cluster0.lemvb4s.mongodb.net/")
db = client.server_db
ad_collection = db.ad_collection

def add_advertisement(detail):
    ad_collection.insert_one(detail)

def get_all_advertisement():
    advertisements_cursor = ad_collection.find({}, {"_id": 0})
    advertisements = dumps(advertisements_cursor)
    return advertisements


def delete_advertisement(id):
    ad_collection.delete_one({"_id": ObjectId(id)})


add_advertisement({"catogory":"Vehical sale","location":"Badulla"})