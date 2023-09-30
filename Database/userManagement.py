from Database.db_connector import db


def deleteUserById(id, dbName=db):
    result = dbName.User.delete_one({"User_ID": id})
    return result.deleted_count > 0


def getAllUsers(dbName=db):
    users = list(dbName.User.find({}, {"_id": 0, "password": 0}))
    return users


def getUserByID(id,dbName=db):
    user = None
    user = dbName.User.find_one({"User_ID": id}, {"_id": 0, "password": 0})
    return user
