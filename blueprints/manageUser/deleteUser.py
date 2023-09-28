from flask import Blueprint, request, jsonify
from Database.userManagement import deleteUserById

deleteUser_bp = Blueprint("deleteUser", __name__)


@deleteUser_bp.route('/delete-user', methods=['POST'])
def delete_user():
    try:
        data = request.get_json()
        user_id = data.get('user_ID')

        if user_id is None:
            return jsonify({"message": "User_ID is required in the JSON payload"}), 400

        success = deleteUserById(user_id)

        if success:
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"message": "User deletion failed"}), 500
    except Exception as e:
        return jsonify({"message": str(e)}), 500
