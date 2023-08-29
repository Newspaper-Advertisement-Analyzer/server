from flask import Flask, request, jsonify, make_response
from NLP.webscraping import scrape_article_data
from NLP.pdf_to_text import extract_text_from_image
from NLP.detailextract import analyze_advertisement
from Database.connecctor import add_advertisement
from Database.connecctor import get_all_advertisement
from Database.userSignUp import add_user,find_user,validate_user
import threading
from NLP.webScaper import extract_article_text

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

@app.route("/signup", methods=["POST"])
def signup():
    email = request.json["email"]
    password = request.json["password"]
    name = request.json["name"]

    print("------------------signup code is called------------------")
    print(email, password,name)

    # add user to the data base
    if find_user(email) is not None :
        return jsonify({"error": "Email already exists"}), 409
        
    success = add_user(name,email,password)
    print("success: ", success)
    if success:
        return jsonify({"message": "Success! You are now registered."})
    else:
        return jsonify({"error": "Error in registering"}), 500

    # verification_code = random.randint(100000, 999999)  # generate_random_code()  # Generate a verification code
    # expiration_time = datetime.now() + timedelta(minutes=1)
    # verification_codes[email] = {
    #     "code": verification_code, "expiration_time": expiration_time}

    # print("verification code: ", verification_code)

    # if (want_send_email):
    #     sendMail(email, verification_code)


    # return jsonify({
    #     "email": new_user["email"]
    # })

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


if __name__ == '__main__':
    app.run(debug=True)
