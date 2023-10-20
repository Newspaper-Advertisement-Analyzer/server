from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
from Database.db_connector import db
from Database.idGenerate import generate_unique_id


def getAverageHousePriceByTimePeriod(time_period, district):
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
                "average_price": {"$avg": {"$toDouble": "$Price"}}
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

    result = list(db.HouseSale_Advertisement.aggregate(pipeline))
    return result


def countHousesale():
    count = db.HouseSale_Advertisement.count_documents({})
    return count


def categorizeHousesaleByCity():
    pipeline = [
        {
            "$match": {
                # Specify the path to the city field
                "Location.City": {"$exists": True},
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
    recent_advertisements = db.HouseSale_Advertisement.find(
        {}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements_list = list(recent_advertisements)

    return advertisements_list


def getRecentHouseSaleAdLocation(duration, limit=15):
    # Define the fields to be extracted
    projection = {
        "_id": 0,  # Exclude the MongoDB document ID
        "Contact_Info": 1,
        "Location": 1,
        "Title": 1,
        "Price": 1,
        "Number_of_Rooms": 1,
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
    recent_advertisements = db.HouseSale_Advertisement.find(
        query, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements_list = list(recent_advertisements)

    return advertisements_list


def getLatestHouseSaleAd(limit=3):
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
    recent_advertisements = db.HouseSale_Advertisement.find(
        {}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisement = recent_advertisements

    return advertisement


def saveHouseSaleAdvertisement(title, location, date, description, image, price, numberOfRooms, postedOn, source, phoneNumbers, email, nearestCity, address, longitude, lattitude):
    # Implement the logic to save land sale advertisements in the database
    # Example code:
    try:
        posted_date = datetime.strptime(date, '%Y-%m-%d')
        result = db.HouseSale_Advertisement.insert_one({
            # Generate a unique ID for the advertisement
            "Advertisement_ID": generate_unique_id(1),
            "Title": title,
            "Posted_Date": posted_date,
            "Description": description,
            "Image": image,
            "Price": price,
            "Number_of_Rooms": int(numberOfRooms),
            "Posted_On": postedOn,
            "Source": source,
            "Contact_Info": {"Phone_Number": [phoneNumbers], "Email": email},
            "Location": {"City": nearestCity, "Longitude": longitude, "Latitude": lattitude},
            "Address": address,
        })
        return result.inserted_id
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
