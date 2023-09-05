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
def getAveragePricebyWeek():
    # Calculate the date 5 weeks ago from today
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(weeks=5)

    # Use $isoWeekYear and $isoWeek to group by week and year
    pipeline = [
        {
            "$match": {
                "Posted_Date": {"$gte": start_date, "$lte": end_date}
            }
        },
        {
            "$addFields": {
                "week": {
                    "$dateToString": {
                        "format": "%Y-%U",  # Format to include year and week number
                        "date": "$Posted_Date"
                    }
                }
            }
        },
        {
            "$group": {
                "_id": "$week",
                "average_price": {"$avg": {"$toDouble": "$Price_per_Perch"}}
            }
        },
        {
            "$sort": {"_id": 1}  # Sort by week start date in ascending order
        }
    ]

    result = list(db.LandSale_Advertisement.aggregate(pipeline))
    #print(result)
   
    return result

def getAveragePricebyMonth():
    # Calculate the date 12 months ago from today
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=365)

    # Use $dateToString to group by month and year
    pipeline = [
        {
            "$match": {
                "Posted_Date": {"$gte": start_date, "$lte": end_date}
            }
        },
        {
            "$addFields": {
                "month": {
                    "$dateToString": {
                        "format": "%Y-%m",  # Format to include year and month
                        "date": "$Posted_Date"
                    }
                }
            }
        },
        {
            "$group": {
                "_id": "$month",
                "average_price": {"$avg": {"$toDouble": "$Price_per_Perch"}}
            }
        },
        {
            "$sort": {"_id": 1}  # Sort by month in ascending order
        }
    ]

    result = list(db.LandSale_Advertisement.aggregate(pipeline))
    return result

def getAveragePricebyYear():
    # Calculate the date 5 years ago from today
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=5*365)

    # Use $dateToString to group by year
    pipeline = [
        {
            "$match": {
                "Posted_Date": {"$gte": start_date, "$lte": end_date}
            }
        },
        {
            "$addFields": {
                "year": {
                    "$dateToString": {
                        "format": "%Y",  # Format to include year
                        "date": "$Posted_Date"
                    }
                }
            }
        },
        {
            "$group": {
                "_id": "$year",
                "average_price": {"$avg": {"$toDouble": "$Price_per_Perch"}}
            }
        },
        {
            "$sort": {"_id": 1}  # Sort by year in ascending order
        }
    ]

    result = list(db.LandSale_Advertisement.aggregate(pipeline))
    return result



def countLandsale():
    count = db.LandSale_Advertisement.count_documents({})
    return count

def getRecentLandSaleAdvertisements(limit=15):
    # Define the fields to be extracted
    projection = {
        "_id": 0,  # Exclude the MongoDB document ID
        "Advertisement_ID": 1,
        "Contact_Info.Phone_Number": 1,
        "Location.City": 1,
        "Posted_Date": 1,
        "Title": 1,
        "Price_per_Perch": 1,
        "Number_of_Perch": 1,
        "Source": 1,
    }

    # Sort the documents by the 'Posted_Date' field in descending order to get the most recent ones first
    recent_advertisements = db.LandSale_Advertisement.find({}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements_list = list(recent_advertisements)

    return advertisements_list

def getRecentLandSaleAdLocation(limit=15):
    # Define the fields to be extracted
    projection = {
        "_id": 0,  # Exclude the MongoDB document ID
        "Contact_Info": 1,
        "Location": 1,
        "Title": 1,
        "Price_per_Perch": 1,
        "Number_of_Perch": 1,
    }

    # Sort the documents by the 'Posted_Date' field in descending order to get the most recent ones first
    recent_advertisements = db.LandSale_Advertisement.find({}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements_list = list(recent_advertisements)

    return advertisements_list

def getLatestLandSaleAd(limit=1):
    # Define the fields to be extracted
    projection = {
        "_id": 0,  # Exclude the MongoDB document ID
         "Advertisement_ID": 1,
        "Title": 1,
        "Price_per_Perch": 1,
        "Number_of_Perch": 1,
        "Description": 1,
    }

    # Sort the documents by the 'Posted_Date' field in descending order to get the most recent ones first
    recent_advertisements = db.LandSale_Advertisement.find({}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements = recent_advertisements

    return advertisements






