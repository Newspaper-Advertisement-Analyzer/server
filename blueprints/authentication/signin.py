# from flask import Blueprint, jsonify, request
# from Database.userSignUp import add_user,find_user,validate_user

# signIn_bp = Blueprint("signin", __name__)

# @signIn_bp.route("/login", methods=["POST"])
# def login_user():
#     email = request.json["email"]
#     password = request.json["password"]

#     print("------------------login code is called------------------")
#     print("email: ", email, "\n", "Pasword: ", password, "\n")

#     if not email or not password:
#         return jsonify({"error": "Email and password are required"}), 400

#     user = find_user(email)
#     if user is None:
#         print("Invalid User Name")
#         return jsonify({"error": "Invalid User Name"}), 401

#     if validate_user(email, password):
#         print("Correct Password")
#         return jsonify({"message": "Success! You are now logged in."})
#     else:
#         print("Incorrect Password")
#         return jsonify({"error": "Incorrect Password"}), 401

from flask import Blueprint, jsonify, request
from Database.userSignUp import add_user, find_user, validate_user

signIn_bp = Blueprint("signin", __name__)


@signIn_bp.route("/login", methods=["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    print("------------------login code is called------------------")
    print("email: ", email, "\n", "Pasword: ", password, "\n")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = find_user(email)
    if user is None:
        print("Invalid User Name")
        return jsonify({"error": "Invalid User Name"}), 401

    if validate_user(email, password):
        print("Correct Password")
        # Create a dictionary with user data (excluding password and _id)
        user_data = {
            "Full_Name": user["Full_Name"],
            "UserID": str(user["_id"]),
            "email": user["email"],
            "Contact_Number": user["Contact_Number"],
            "User_Name": user["User_Name"],
            "Registration_Date": user["Registration_Date"],
            "Profession": user["Profession"],
            "Role": user["Role"],
            "Profile_Picture": user["Profile_Picture"] if "Profile_Picture" in user else None
        }
        return jsonify({"message": "Success! You are now logged in.", "user": user_data})
    else:
        print("Incorrect Password")
        return jsonify({"error": "Incorrect Password"}), 401
