from flask import Blueprint, Flask, request, jsonify

from Database.userSignUp import find_user, replace_password
from datetime import datetime, timedelta
from sendEmail.sendVerificstionCode import send_advanced_email
import random

reset_password_bp = Blueprint("resetPSW", __name__)
verification_codes = {}
pending_registrations = {}


@reset_password_bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data.get('email')
    print("Received email:", email)

    # You can perform additional actions here, such as sending a reset email.

    user = find_user(email)
    if user is None:
        print("Invalid User Name")
        return jsonify({"error": "Invalid User Name"}), 401
    else:
        verification_code = random.randint(100000, 999999)
        expiration_time = datetime.now() + timedelta(minutes=1)
        pending_registrations[email] = {
            "code": verification_code,
            "expiration_time": expiration_time,
        }

        print("verification code for reset password: ", verification_code)

        # send email to the user
        # send_advanced_email(email, verification_code)

        return jsonify({"message": "Verification code sent."})

    response_data = {"message": "Email received successfully"}
    return jsonify(response_data)


@reset_password_bp.route("/verify-email", methods=["POST"])
def verify():
    email = request.json["email"]
    user_code = request.json["verificationCode"]
    cancel = request.json.get("cancel", False)  # Check for the cancel flag

    if email in pending_registrations:
        stored_code = pending_registrations[email]["code"]
        expiration_time = pending_registrations[email]["expiration_time"]

        if not cancel and datetime.now() < expiration_time and int(user_code.strip()) == stored_code:
            del pending_registrations[email]
            print("Verification successful")
            new_password = random.randint(100000, 999999)
            replace_password(email, str(new_password))
            return jsonify({"success": True, "newpassword": new_password})
        else:
            del pending_registrations[email]
            print("Registration failed")
            return jsonify({"success": False})
    else:
        print("Registration failed")
        return jsonify({"success": False})


@reset_password_bp.route("/new-password", methods=["POST"])
def new_password():

    password = request.json["password"]
    print("Received password:", password)
    return jsonify({"message": "Password received successfully"})
