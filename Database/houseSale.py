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


def getRecentHouseSaleAdvertisements(limit=15):
    # Define the fields to be extracted
    projection = {
        "_id": 0,  # Exclude the MongoDB document ID
        "Advertisement_ID": 1,
        "Contact_Info.Phone_Number": 1,
        "Location.City": 1,
        "Posted_Date": 1,
        "Title": 1,
        "Price": 1,
        "Number_of_Rooms": 1,
        "Source": 1
    }

    # Sort the documents by the 'Posted_Date' field in descending order to get the most recent ones first
    recent_advertisements = db.HouseSale_Advertisement.find({}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements_list = list(recent_advertisements)

    return advertisements_list


def getRecentHouseSaleAdLocation(limit=15):
    # Define the fields to be extracted
    projection = {
        "_id": 0,  # Exclude the MongoDB document ID
        "Contact_Info": 1,
        "Location": 1,
        "Title": 1,
        "Price": 1,
        "Number_of_Rooms": 1,
    }

    # Sort the documents by the 'Posted_Date' field in descending order to get the most recent ones first
    recent_advertisements = db.HouseSale_Advertisement.find({}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements_list = list(recent_advertisements)

    return advertisements_list
