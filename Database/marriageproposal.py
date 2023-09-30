from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
from Database.db_connector import db


def countMarriageProposals():
    count = db.HouseSale_Advertisement.count_documents({})
    return count


def categorizeMarriageProposalsByAge():
    pipeline = [
        {
            "$match": {
                # Assuming age information is stored in the 'age' field
                "Age": {"$exists": True},
            }
        },
        {
            "$bucket": {
                "groupBy": "$Age",
                # Define your age categories as needed
                "boundaries": [18, 25, 30, 35, 40],
                "default": "Other",  # If age doesn't fall into any category, categorize as 'Other'
                "output": {
                    "count": {"$sum": 1}
                }
            }
        }
    ]

    result = list(db.Marriage_Proposal.aggregate(pipeline))
    print(result)
    return result


def categorizeMarriageProposalsByProfession():
    pipeline = [
        {
            "$match": {
                # Assuming profession information is stored in the 'Profession' field
                "Profession": {"$exists": True},
            }
        },
        {
            "$group": {
                "_id": "$Profession",  # Group by the 'Profession' field
                # Count the occurrences of each profession type
                "count": {"$sum": 1}
            }
        },
        {
            # Sort the results by count in descending order
            "$sort": {"count": -1}
        }
    ]

    result = list(db.Marriage_Proposal.aggregate(pipeline))
    return result


def categorizeMarriageProposalsByCity():
    pipeline = [
        {
            "$match": {
                # Assuming profession information is stored in the 'Profession' field
                "Location.City": {"$exists": True},
            }
        },
        {
            "$group": {
                "_id": "$Location.City",  # Group by the 'Profession' field
                # Count the occurrences of each profession type
                "count": {"$sum": 1}
            }
        },
        {
            # Sort the results by count in descending order
            "$sort": {"count": -1}
        }
    ]

    result = list(db.Marriage_Proposal.aggregate(pipeline))
    return result


def getRecentMarriageProposals(limit=15):
    # Define the fields to be extracted
    projection = {
        "_id": 0,  # Exclude the MongoDB document ID
        "Advertisement_ID": 1,
        "Contact_Info.Phone_Number": 1,
        "Location.City": 1,
        "Posted_Date": 1,
        "Title": 1,
        "Gender": 1,
        "Age": 1,
        "Profession": 1,
        "Nationality": 1,
        "Source": 1
    }

    # Sort the documents by the 'Posted_Date' field in descending order to get the most recent ones first
    recent_advertisements = db.Marriage_Proposal.find(
        {}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements_list = list(recent_advertisements)

    return advertisements_list


def getRecentMarriagePropLocation(duration, limit=15):
    # Define the fields to be extracted
    projection = {
        "_id": 0,  # Exclude the MongoDB document ID
        "Contact_Info": 1,
        "Location": 1,
        "Title": 1,
        "Gender": 1,
        "Age": 1,
        "Profession": 1,
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
    recent_advertisements = db.Marriage_Proposal.find(
        query, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements_list = list(recent_advertisements)

    return advertisements_list


def getLatestMarriageProposalSaleAd(limit=2):
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
    recent_advertisements = db.Marriage_Proposal.find(
        {}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements = recent_advertisements

    return advertisements
