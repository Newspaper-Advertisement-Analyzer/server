from Database.db_connector import db

def deleteUserById(id):
    db.User.delete_one({"_id": id})
    return True

def getAllUsers():
    users = list(db.User.find({},{"_id": 0}))
    return users