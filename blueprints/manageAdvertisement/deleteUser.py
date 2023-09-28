from flask import Blueprint, request, jsonify
from Database.user import deleteUser

deleteUser_bp = Blueprint("deleteUser", __name__)


@deleteUser_bp.route('/getAverageLandPrice', methods=['POST'])
def deleteUser():
    user_ID = request.args.get('user_ID')
    succes = deleteUser(user_ID)
    if succes:  # If the user was deleted successfully
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User deletion failed"}), 500
