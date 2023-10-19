from Database.db_connector import db
from bson import ObjectId


def getAllPendingAds(dbName=db):
    ads = list(dbName.Pending_Advertisement.find({}, {"_id": 0}))
    print(ads)
    return ads


def add_pending_advertisement(ad_data, dbName=db):
    # db.Pending_Advertisement.insert_one(ad_data)
    ad = {
        "Advertisement_ID": "ad8000",
        "Title": ad_data[0],
        "Description": ad_data[2],
        "Location": {"City": ad_data[7]},
        "Category": ad_data[4],
        "Contact_Info": {
            "Phone": ad_data[6],
            "Email": ad_data[8]
        },
        "price": ad_data[5],
        "Posted_Date": ad_data[-1]
    }
    dbName.Pending_Advertisement.insert_one(ad)
    return True
