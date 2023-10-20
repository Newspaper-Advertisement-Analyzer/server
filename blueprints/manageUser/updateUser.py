import bcrypt
from flask import Blueprint, request, jsonify
from Database.userManagement import getUserByID, updateUserById, getUserByIDPass

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
            "password": data.get("password"),
        }
        print(update_data)
        # Assuming you have a function to retrieve user data by ID
        user = getUserByIDPass(user_id)
        print(user)
        password_updated = False
        if user and 'password' in data and data['password']:
            new_password = data['password']
            if not bcrypt.checkpw(new_password.encode('utf-8'), user['password'].encode('utf-8')):
                hashed_password = bcrypt.hashpw(new_password.encode(
                    'utf-8'), bcrypt.gensalt()).decode('utf-8')
                update_data["password"] = hashed_password
                password_updated = True

        if updateUserById(user_id, update_data):
            if password_updated:
                return jsonify({"message": "User information updated successfully", "password_updated": True})
            else:
                return jsonify({"message": "User information updated successfully", "password_updated": False})
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
