from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
import datetime
import os
from Database.db_connector import db

def getAverageHousePriceByTimePeriod(time_period, district):
    # Define time_period_to_timedelta mapping
    time_period_to_timedelta = {
        "Weekly": datetime.timedelta(weeks=5),
        "Monthly": datetime.timedelta(days=365 / 12),  # Approximately 30.44 days per month
        "Yearly": datetime.timedelta(days=365),
    }

    # Calculate the date based on the specified time_period
    end_date = datetime.datetime.now()
    start_date = end_date - time_period_to_timedelta.get(time_period, datetime.timedelta(days=365))

    # Define the date format for grouping
    date_format = {
        "Weekly": "%Y-%U",
        "Monthly": "%Y-%m",
        "Yearly": "%Y",
    }.get(time_period, None)

    if not date_format:
        return []

    # Define the initial pipeline without the $match stage
    pipeline = [
        {
            "$addFields": {
                time_period: {
                    "$dateToString": {
                        "format": date_format,
                        "date": "$Posted_Date"
                    }
                }
            }
        },
        {
            "$group": {
                "_id": f"${time_period}",
                "average_price": {"$avg": {"$toDouble": "$Price"}}
            }
        },
        {
            "$sort": {"_id": 1}  # Sort by the specified time period in ascending order
        }
    ]

    # Conditionally include the $match stage if district is not "Overall"
    if district != "Overall":
        pipeline.insert(0, {
            "$match": {
                "Posted_Date": {"$gte": start_date, "$lte": end_date},
                "Location.City": district
            }
        })

    result = list(db.HouseSale_Advertisement.aggregate(pipeline))
    return result



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


def getLatestHouseSaleAd(limit=1):
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
    recent_advertisements = db.HouseSale_Advertisement.find({}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisement = recent_advertisements

    return advertisement