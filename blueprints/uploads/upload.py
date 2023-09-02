from flask import Blueprint, request, jsonify, make_response, current_app
from Database.userSignUp import add_user,find_user,validate_user
from NLP.webscraping import scrape_article_data
from NLP.pdf_to_text import extract_text_from_image
from NLP.detailextract import analyze_advertisement
from Database.adCollection import add_advertisement

import threading
from NLP.webScraper import extract_article_info
from flask import Flask,make_response,send_from_directory
# from NLP.oldwebScaper import extract_article_text
from NLP.webScraper import extract_article_info
from werkzeug.utils import secure_filename
import os

upload_bp = Blueprint("upload", __name__)

@upload_bp.route('/members', methods=['POST','GET'])
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

@upload_bp.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})

    image = request.files['image']
    image_path = 'uploaded_image.png'
    image.save(image_path)

    extracted_text = extract_text_from_image(image_path)
    return jsonify({'extracted_text': extracted_text})

@upload_bp.route('/sendurl', methods=['POST'])
def receive_url_from_frontend():
    data = request.get_json()
    url = data.get('url')

    results = extract_article_info(url)

    print(url)

    return jsonify({'results': results})

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/upload', methods=['POST'])
def upload_image():
    print("upload_multiple_images is called")
    
    if 'images' not in request.files:
        return jsonify({'error': 'No images part'})

    images = request.files.getlist('images')  # Use getlist to retrieve multiple files

    for image in images:
        if image.filename == '':
            # Skip empty files
            continue

        if not allowed_file(image.filename):
            return jsonify({'error': 'Invalid file type'})

        filename = secure_filename(image.filename)
        
        upload_folder = current_app.config['UPLOAD_FOLDER']  # Access the config from the current app
        image.save(os.path.join(upload_folder, filename))
    return jsonify({'message': 'Image uploaded successfully'})

