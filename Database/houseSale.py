from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
import datetime
import os


load_dotenv('./.env')

username: str = os.getenv('DBUSERNAME')
password: str = os.getenv('PASSWORD')

client = MongoClient("mongodb+srv://"+username+":"+password +"@cluster0.lemvb4s.mongodb.net/")
db = client.Advizor

def countHousesale():
    count = db.HouseSale_Advertisement.count_documents({})
    return count

def categorizeHousesaleByCity():
    pipeline = [
        {
            "$match": {
                "Location.City": {"$exists": True},  # Specify the path to the city field
            }
        },
        {
            "$group": {
                "_id": "$Location.City",  # Use the correct path to the city field
                "count": {"$sum": 1}
            }
        }
    ]

    result = list(db.HouseSale_Advertisement.aggregate(pipeline))
    return result
