from flask import Blueprint, jsonify, request
from datetime import datetime, timedelta
from Database.userSignUp import add_user, find_user, validate_user
from sendEmail.sendVerificstionCode import send_advanced_email
import random
from bson.objectid import ObjectId

verification_codes = {}
pending_registrations = {}

signUp_bp = Blueprint("signup", __name__)


@signUp_bp.route("/signup", methods=["POST"])
def signup():
    email = request.json["email"]
    password = request.json["password"]
    name = request.json["name"]

    print("------------------signup code is called------------------")
    print(email, password, name)

    if find_user(email) is not None:
        return jsonify({"error": "Email already exists"}), 409

    verification_code = random.randint(100000, 999999)
    expiration_time = datetime.now() + timedelta(minutes=1)
    pending_registrations[email] = {
        "code": verification_code,
        "expiration_time": expiration_time,
        "name": name,
        "password": password,
    }

    print("verification code: ", verification_code)

    # send email to the user
    send_advanced_email(email, verification_code)

    return jsonify({"message": "Verification code sent."})


@signUp_bp.route("/verify", methods=["POST"])
def verify():
    email = request.json["email"]
    user_code = request.json["verificationCode"]
    cancel = request.json.get("cancel", False)  # Check for the cancel flag

    if email in pending_registrations:
        stored_code = pending_registrations[email]["code"]
        expiration_time = pending_registrations[email]["expiration_time"]

        if not cancel and datetime.now() < expiration_time and int(user_code.strip()) == stored_code:
            user_data = pending_registrations[email]
            add_user(user_data["name"], email, user_data["password"])
            del pending_registrations[email]
            print("Registration successful")
            user = find_user(email)
            user_data = {
                "Full_Name": user["Full_Name"],
                "UserID": str(user["_id"]),
                "email": user["email"],
                "Contact_Number": user["Contact_Number"],
                "User_Name": user["User_Name"],
                "Registration_Date": user["Registration_Date"],
                "Profession": user["Profession"],
                "Role": user["Role"]
            }
            return jsonify({"success": True, "user": user_data})
        else:
            del pending_registrations[email]
            print("Registration failed")
            return jsonify({"success": False})
    else:
        print("Registration failed")
        return jsonify({"success": False})
