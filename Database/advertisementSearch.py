from pymongo import MongoClient
from bson.json_util import dumps
from dotenv import load_dotenv
import datetime
from datetime import datetime
import os

load_dotenv('./.env')

username = os.getenv('DBUSERNAME')
password = os.getenv('PASSWORD')

client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.lemvb4s.mongodb.net/")
db = client.Advizor



def search_ads_by_date(start_date, end_date):
    # Convert start_date and end_date to datetime objects
    start_date_obj = datetime.fromisoformat(start_date)
    end_date_obj = datetime.fromisoformat(end_date)

    # Initialize an empty list to store the results
    results = []
    # List of advertisement collections
    collections = ["LandSale_Advertisement", "HouseSale_Advertisement", "Marriage_Proposal"]

    # Iterate through each collection and perform the search
    for collection_name in collections:
        # Define the aggregation pipeline for the current collection
        pipeline = [
            {
                "$match": {
                    "Posted_Date": {
                        "$gte": start_date_obj,  # Greater than or equal to start_date
                        "$lte": end_date_obj    # Less than or equal to end_date
                    }
                }
            },
            {
                "$project": {
                    "_id": 0  # Exclude the Object ID from the results
                }
            }
        ]

        # Execute the aggregation for the current collection
        collection_results = list(db[collection_name].aggregate(pipeline))

        # Add the results to the overall results list
        results.extend(collection_results)

    return results





def search_ads_by_category(collection_name):
    projection = {"_id": 0}
    results = list(db[collection_name].find({}, projection))
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


def search_ads_by_location(location):

    # Initialize an empty list to store the results
    results = []
    # List of advertisement collections
    collections = ["LandSale_Advertisement", "HouseSale_Advertisement", "Marriage_Proposal"]
    regex_pattern = f".*{location}.*"

    # Iterate through each collection and perform the search
    for collection_name in collections:
        # Define the aggregation pipeline for the current collection
        pipeline = [
            {
                 "$match": {
                    "Location.City": {
                        "$regex": regex_pattern,
                        "$options": "i"  # Case-insensitive
                    }
                }
            },
            {
                "$project": {
                    "_id": 0  # Exclude the Object ID from the results
                }
            }
        ]

        # Execute the aggregation for the current collection
        collection_results = list(db[collection_name].aggregate(pipeline))

        # Add the results to the overall results list
        results.extend(collection_results)

    return results


def search_ads_by_title(title):

    # Initialize an empty list to store the results
    results = []
    # List of advertisement collections
    collections = ["LandSale_Advertisement", "HouseSale_Advertisement", "Marriage_Proposal"]
    regex_pattern = f".*{title}.*"
    # Iterate through each collection and perform the search
    for collection_name in collections:
        # Define the aggregation pipeline for the current collection
        pipeline = [
            {
                 "$match": {
                    "Title": {
                        "$regex": regex_pattern,
                        "$options": "i"  # Case-insensitive
                    }
                }
            },
            {
                "$project": {
                    "_id": 0  # Exclude the Object ID from the results
                }
            }
        ]

        # Execute the aggregation for the current collection
        collection_results = list(db[collection_name].aggregate(pipeline))

        # Add the results to the overall results list
        results.extend(collection_results)

    return results

