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


def countLandsale():
    count = db.LandSale_Advertisement.count_documents({})
    return count
