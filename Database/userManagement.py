from Database.db_connector import db
from bson import ObjectId


def deleteUserById(id, dbName=db):
    result = dbName.User.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0


def getAllUsers(dbName=db):
    users = list(dbName.User.find({}, {"password": 0}))
    serialized_users = []
    for user in users:
        serialized_user = {**user, '_id': str(user['_id'])}
        serialized_users.append(serialized_user)
    return serialized_users


def getUserByID(id, dbName=db):
    user = None
    user = dbName.User.find_one({"password": 0})
    return user


def updateUserById(id, update_data, dbName=db):
    result = dbName.User.update_one(
        {"_id": ObjectId(id)}, {"$set": update_data}, upsert=False)
    return result.modified_count > 0
