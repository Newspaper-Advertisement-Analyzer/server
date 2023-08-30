from flask import Blueprint, jsonify, request
from Database.userSignUp import add_user,find_user,validate_user

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
        return jsonify({"message": "Success! You are now logged in."})
    else:
        print("Incorrect Password")
        return jsonify({"error": "Incorrect Password"}), 401

