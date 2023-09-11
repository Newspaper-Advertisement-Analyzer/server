from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
import datetime
import os
from Database.db_connector import db

def countMarriageProposals():
    count = db.HouseSale_Advertisement.count_documents({})
    return count

def categorizeMarriageProposalsByAge():
    pipeline = [
        {
            "$match": {
                "Age": {"$exists": True},  # Assuming age information is stored in the 'age' field
            }
        },
        {
            "$bucket": {
                "groupBy": "$Age",
                "boundaries": [18, 25, 30, 35, 40],  # Define your age categories as needed
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
                "Profession": {"$exists": True},  # Assuming profession information is stored in the 'Profession' field
            }
        },
        {
            "$group": {
                "_id": "$Profession",  # Group by the 'Profession' field
                "count": {"$sum": 1}  # Count the occurrences of each profession type
            }
        },
        {
            "$sort": {"count": -1}  # Sort the results by count in descending order
        }
    ]

    result = list(db.Marriage_Proposal.aggregate(pipeline))
    return result


def categorizeMarriageProposalsByCity():
    pipeline = [
        {
            "$match": {
                "Location.City": {"$exists": True},  # Assuming profession information is stored in the 'Profession' field
            }
        },
        {
            "$group": {
                "_id": "$Location.City",  # Group by the 'Profession' field
                "count": {"$sum": 1}  # Count the occurrences of each profession type
            }
        },
        {
            "$sort": {"count": -1}  # Sort the results by count in descending order
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
    recent_advertisements = db.Marriage_Proposal.find({}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements_list = list(recent_advertisements)

    return advertisements_list


def getRecentMarriagePropLocation(limit=15):
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

    # Sort the documents by the 'Posted_Date' field in descending order to get the most recent ones first
    recent_advertisements = db.Marriage_Proposal.find({}, projection).sort("Posted_Date", -1).limit(limit)

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
    recent_advertisements = db.Marriage_Proposal.find({}, projection).sort("Posted_Date", -1).limit(limit)

    # Convert the cursor to a list of dictionaries
    advertisements = recent_advertisements

    return advertisements
