from Database.db_connector import db
from bson import ObjectId


def getAllPendingAds(dbName=db):
    ads = list(dbName.Pending_Advertisement.find({}, {"_id": 0}))
    return ads
