from flask import Flask, request, jsonify, make_response
from NLP.webscraping import scrape_article_data
from NLP.pdf_to_text import extract_text_from_image
from NLP.detailextract import analyze_advertisement
from Database.connecctor import add_advertisement
from Database.connecctor import get_all_advertisement
from Database.userSignUp import add_user,find_user,validate_user
import threading
from NLP.webScaper import extract_article_text
from flask import Flask,make_response,send_from_directory
# from NLP.oldwebScaper import extract_article_text
from NLP.webScraper import extract_article_info

app = Flask(__name__)

@app.route('/members', methods=['POST','GET'])
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
        add_advertisement(ad_data)

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
    markers = get_all_advertisement()
    return jsonify(markers)

@app.route('/serviceWorker.js')
def get_service_worker():
    #in this case serviceWorker.js is stored in the root of the project
    #You can enter the name of directory in which this file is stored
    response = make_response(send_from_directory('','serviceWorker.js'))
    response.headers['Content-Type'] = 'application/javascript'
    return response
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
