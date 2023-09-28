from flask import Blueprint, request, jsonify
from Database.userManagement import getAllUsers

getAllUsers_bp = Blueprint("getAllUsers", __name__)


@getAllUsers_bp.route('/getAllUsers', methods=['GET'])
def get_all_users():
    try:
        users = list(getAllUsers())
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
