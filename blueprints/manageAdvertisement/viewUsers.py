from flask import Blueprint, request, jsonify
from Database.user import getAllUsers

getAllUsers_bp = Blueprint("getAllUsers", __name__)


def getAllUsers():
    users = list(db.User.find({}, {"_id": 0}))
    return users
