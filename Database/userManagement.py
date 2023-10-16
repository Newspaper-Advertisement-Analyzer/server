from Database.db_connector import db
from bson import ObjectId


def deleteUserById(id, dbName=db):
    result = dbName.User.delete_one({"User_ID": id})
    return result.deleted_count > 0


def getAllUsers(dbName=db):
    users = list(dbName.User.find({}, {"_id": 0, "password": 0}))
    return users


def getUserByID(id, dbName=db):
    user = None
    user = dbName.User.find_one({"User_ID": id}, {"_id": 0, "password": 0})
    return user


def updateUserById(id, update_data, dbName=db):
    result = dbName.User.update_one(
        {"_id": ObjectId(id)}, {"$set": update_data}, upsert=False)
    return result.modified_count > 0
