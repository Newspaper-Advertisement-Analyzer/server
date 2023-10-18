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


@updateUser_bp.route('/updateProfilePicture', methods=['POST'])
def update_profile_picture():
    try:
        data = request.get_json()
        # Ensure you are getting the correct user ID
        user_id = data.get("userId")
        update_data = {
            "Profile_Picture": data.get("url"),
        }
        if updateUserById(user_id, update_data):
            return jsonify({"message": "User information updated successfully"})
        else:
            return jsonify({"error": "Failed to update user information"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@updateUser_bp.route('/updateLastSeen', methods=['POST'])
def update_last_seen():
    try:
        data = request.get_json()
        # Ensure you are getting the correct user ID
        user_id = data.get("userId")
        update_data = {
            "Last_Seen": data.get("last_seen"),
        }
        if updateUserById(user_id, update_data):
            return jsonify({"message": "User information updated successfully"})
        else:
            return jsonify({"error": "Failed to update user information"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
