from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
from datetime import datetime
import os
from Database.db_connector import db


# Define a function to save the feedback in the database
def saveFeedback(rating, feedback, publish, userID):
    collection = db.Feedback

    # Create a dictionary containing the feedback data
    feedback_data = {
        "rating": rating,
        "feedback": feedback,
        "publish": publish,
        "userID": userID,
        "timestamp": datetime.now()
    }

    # Insert the feedback data into the collection
    result = collection.insert_one(feedback_data)

    return result.inserted_id


def getAllPublishedFeedbacks():
    collection = db.Feedback

    # Define the query to filter the documents where "publish" is true
    query = {"publish": True}

    # Retrieve all feedbacks where "publish" is true
    published_feedbacks = list(collection.find(query))

    # Convert the ObjectId to string for each document
    for feedback in published_feedbacks:
        feedback["_id"] = str(feedback["_id"])

    return published_feedbacks
