from datetime import datetime, timedelta
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
# Import datetime and timedelta from datetime module
from datetime import datetime, timedelta
import os
from Database.db_connector import db


def getAverageLandPriceByTimePeriod(time_period, district):
    # Define time_period_to_timedelta mapping
    time_period_to_timedelta = {
        "Weekly": timedelta(weeks=5),
        # Approximately 30.44 days per month
        "Monthly": timedelta(days=365 / 12),
        "Yearly": timedelta(days=365),
    }

    # Calculate the date based on the specified time_period
    end_date = datetime.now()
    start_date = end_date - \
        time_period_to_timedelta.get(time_period, timedelta(days=365))

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
                "average_price": {"$avg": {"$toDouble": "$Price_per_Perch"}}
            }
        },
        {
            # Sort by the specified time period in ascending order
            "$sort": {"_id": 1}
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
    recent_advertisements = db.LandSale_Advertisement.find(
        {}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements_list = list(recent_advertisements)

    return advertisements_list


def getRecentLandSaleAdLocation(duration, limit=15):
    # Define the fields to be extracted
    projection = {
        "_id": 0,  # Exclude the MongoDB document ID
        "Contact_Info": 1,
        "Location": 1,
        "Title": 1,
        "Price_per_Perch": 1,
        "Number_of_Perch": 1,
    }

    # Calculate the start date based on the selected duration
    if duration == "Overall":
        # No date filter needed, retrieve all records
        start_date = None
    elif duration == "Today":
        # Retrieve records from today onwards
        start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    elif duration == "Yesterday":
        # Retrieve records from yesterday
        start_date = datetime.now().replace(hour=0, minute=0, second=0,
                                            microsecond=0) - timedelta(days=1)
    elif duration == "LastWeek":
        # Retrieve records from the start of the previous week
        today = datetime.now()
        start_date = today - timedelta(days=today.weekday() + 7)
    elif duration == "LastMonth":
        # Retrieve records from the start of the previous month
        today = datetime.now()
        start_date = today.replace(day=1) - timedelta(days=1)

    # Create a filter based on the start date
    if start_date:
        date_filter = {"Posted_Date": {"$gte": start_date}}
    else:
        date_filter = {}

    # Add the date filter to the query
    query = {"$and": [date_filter]}

    # Sort the documents by the 'Posted_Date' field in descending order to get the most recent ones first
    recent_advertisements = db.LandSale_Advertisement.find(
        query, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements_list = list(recent_advertisements)

    return advertisements_list


def getLatestLandSaleAd(limit=3):
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
    recent_advertisements = db.LandSale_Advertisement.find(
        {}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements = recent_advertisements

    return advertisements
