from flask import Blueprint, request, jsonify
from Database.userManagement import getUserByID, updateUserById

updateUser_bp = Blueprint("updateUser", __name__)

# Add the update function to update the user


@updateUser_bp.route('/updateUser', methods=['POST'])
def update_user():
    try:
        data = request.get_json()
        user_id = data.get("userId")
        update_data = {
            "Full_Name": data.get("fullName"),
            "Contact_Number": data.get("mobile"),
            "Profession": data.get("profession"),

        }
        print(user_id)
        if updateUserById(user_id, update_data):
            return jsonify({"message": "User information updated successfully"})
        else:
            return jsonify({"error": "Failed to update user information"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
