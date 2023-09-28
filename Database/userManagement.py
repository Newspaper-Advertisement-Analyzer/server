from Database.db_connector import db


def deleteUserById(id):
    result = db.User.delete_one({"User_ID": id})
    return result.deleted_count > 0


def getAllUsers():
    users = list(db.User.find({}, {"_id": 0, "password": 0}))
    return users


def getUserByID(id):
    user = None
    user = db.User.find_one({"User_ID": id}, {"_id": 0, "password": 0})
    return user
