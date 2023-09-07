from pymongo import MongoClient
from bson.json_util import dumps
from dotenv import load_dotenv
import datetime
import os

load_dotenv('./.env')

username = os.getenv('DBUSERNAME')
password = os.getenv('PASSWORD')

client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.lemvb4s.mongodb.net/")
db = client.Advizor

def search_ads_by_filters(date):
    # Define the common match criteria for the aggregation pipeline
    match_criteria = {
        "collectionNameField": "LandSale_Advertisement",
        "postDate": date  # Pass a valid datetime object here
    }

    # Define the aggregation pipeline
    pipeline = [
        {
            "$match": match_criteria
        },
        {
            "$unionWith": {
                "coll": "LandSale_Advertisement",
                "pipeline": [
                    {
                        "$match": {
                            "postDate": date  # Pass a valid datetime object here
                        }
                    }
                ]
            }
        },
        {
            "$unionWith": {
                "coll": "HouseSale_Advertisement",
                "pipeline": [
                    {
                        "$match": {
                            "postDate": date  # Pass a valid datetime object here
                        }
                    }
                ]
            }
        },
        {
            "$unionWith": {
                "coll": "Marriage_Proposals",
                "pipeline": [
                    {
                        "$match": {
                            "postDate": date  # Pass a valid datetime object here
                        }
                    }
                ]
            }
        }
    ]

    # Execute the aggregation
    results = list(db.LandSale_Advertisement.aggregate(pipeline))
    print(results)

    # Filter results based on the search query (title or location)

    return results


def get_ads_by_category(category, start_date, end_date):
    # Define the match criteria for the aggregation pipeline
    match_criteria = {
        "postDate": {
            "$gte": start_date,
            "$lte": end_date
        }
    }

    # Define the aggregation pipeline
    pipeline = [
        {
            "$match": match_criteria
        }
    ]

    # Execute the aggregation
    results = list(db[category].aggregate(pipeline))

    return results


def searchADbyID(adID, AdvertisementCollection):
    print(adID)
    try:
        # Find the advertisement document by its Advertisement_ID
        advertisement = db[AdvertisementCollection].find_one(
            {"Advertisement_ID": adID},
            {"_id": 0}  # Exclude the "_id" field
        )
        if advertisement:
            return advertisement
        else:
            return None
    except Exception as e:
        print("Error searching advertisement by ID:", str(e))
        return None
