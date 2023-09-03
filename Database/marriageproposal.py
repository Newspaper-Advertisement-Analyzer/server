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

