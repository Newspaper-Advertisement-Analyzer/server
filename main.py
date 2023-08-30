from flask import Flask, request, jsonify, make_response
from NLP.webscraping import scrape_article_data
from NLP.pdf_to_text import extract_text_from_image
from NLP.detailextract import analyze_advertisement
from Database.connecctor import add_advertisement
from Database.connecctor import get_all_advertisement
from Database.userSignUp import add_user,find_user,validate_user,delete_user
import threading
# from NLP.oldwebScaper import extract_article_text
from NLP.webScraper import extract_article_info

from datetime import datetime, timedelta
import random

from sendEmail.sendVerificstionCode import send_advanced_email

verification_codes = {}


app = Flask(__name__)

@app.route('/members', methods=['POST'])
def members():
    inp = request.json.get("inp")
    print(inp) # this is the URl
    try:
        # article_data = scrape_article_data(inp)
        # print("link is ",article_data) this is wrong

        
        location, category, contact_info, prices = analyze_advertisement(inp)
        ad_data = {
            "position": "Default",
            "name": "Default",
            "location": location,
            "category": category,
            "phoneNumber": contact_info["phone_numbers"],
            "email": contact_info["email_addresses"],
            "price": prices
        }
        
        # Create a new thread for the add_advertisement function
        # thread = threading.Thread(target=add_advertisement, args=(ad_data,))
        # thread.start()

        # Create a JSON response with the required headers
        return jsonify(ad_data)
    except Exception as e:
        return jsonify(error=str(e))

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    image = request.files['image']
    image_path = 'uploaded_image.png'
    image.save(image_path)

    extracted_text = extract_text_from_image(image_path)
    return jsonify({'extracted_text': extracted_text})

@app.route("/get_marker_locations", methods=['GET'])
def get_markers():
    print("hi")
    markers = get_all_advertisement()
    print(markers)
    return jsonify(markers)


pending_registrations = {}
@app.route("/signup", methods=["POST"])
def signup():
    email = request.json["email"]
    password = request.json["password"]
    name = request.json["name"]

    print("------------------signup code is called------------------")
    print(email, password,name)

    if find_user(email) is not None :
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


@app.route("/verify", methods=["POST"])
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
            return jsonify({"success": True})
        else:
            del pending_registrations[email]
            print("Registration failed")
            return jsonify({"success": False})
    else:
        print("Registration failed")
        return jsonify({"success": False})

@app.route("/login", methods=["POST"])
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

@app.route('/sendurl', methods=['POST'])
def receive_url_from_frontend():
    data = request.get_json()
    url = data.get('url')

    results = extract_article_info(url)

    print(url)

    return jsonify({'results': results})

from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_image():
    print("upload image is called")
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'})

    image = request.files['image']

    if image.filename == '':
        # set a name for the image
        image.filename = 'image.jpg'
        return jsonify({'error': 'No name but saved as image.jpg'})
        # return jsonify({'error': 'No selected image'})

    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({'message': 'Image uploaded successfully'})



if __name__ == '__main__':
    app.run(debug=True)
