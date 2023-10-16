from flask import Blueprint, request, jsonify, make_response, current_app
from Database.userSignUp import add_user, find_user, validate_user
from NLP.webscraping import scrape_article_data
from NLP.pdf_to_text import extract_text_from_image
from NLP.detailextract import analyze_advertisement
from NLP.detailextract import analyze_advertisement_img
from NLP.pdf_to_text import pdftotext
from NLP.pdf_to_text import pdftotext_ocr


# import threading
from NLP.webScraper import extract_article_info
# from flask import Flask, make_response, send_from_directory
# from NLP.oldwebScaper import extract_article_text
from NLP.webScraper import extract_article_info
from werkzeug.utils import secure_filename
import os

upload_bp = Blueprint("upload", __name__)


@upload_bp.route('/members', methods=['POST', 'GET'])
def members():
    inp = request.json.get("inp")
    print("link is ",inp)  # this is the URl
    try:
        # article_data = scrape_article_data(inp)
        # print("link is ",article_data) this is wrong

        print("analyze_advertisement is going to run")
        
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

    # Use getlist to retrieve multiple files
    images = request.files.getlist('images')
    result = []
    for image in images:
        if image.filename == '':
            # Skip empty files
            continue

        if not allowed_file(image.filename):
            return jsonify({'error': 'Invalid file type'})

        filename = secure_filename(image.filename)

        # Access the config from the current app
        upload_folder = current_app.config['UPLOAD_FOLDER_IMG']
        image.save(os.path.join(upload_folder, filename))
        extracted_text = (extract_text_from_image(
            os.path.join(upload_folder, filename)))
        result.append(analyze_advertisement_img(extracted_text))
    return jsonify({'message': result})
    # return jsonify({'message': 'Image uploaded successfully'})


ALLOWED_EXTENSIONS_PDF = {'pdf'}


def allowed_pdf(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_PDF


@upload_bp.route('/uploadpdf', methods=['POST'])
def upload_pdf():
    isImageContained = request.args.get('isImageContained')
    print(isImageContained)

    if 'pdfs' not in request.files:
        return jsonify({'error': 'No pdfs part'})

    # Use getlist to retrieve multiple files
    pdfs = request.files.getlist('pdfs')
    result = []
    for pdf in pdfs:
        if pdf.filename == '':
            # Skip empty files
            continue

        if not allowed_pdf(pdf.filename):
            return jsonify({'error': 'Invalid file type'})

        filename = secure_filename(pdf.filename)

        # Access the config from the current app
        upload_folder = current_app.config['UPLOAD_FOLDER_PDF']
        pdf.save(os.path.join(upload_folder, filename))

        if (isImageContained=="true"):
            extracted_text = (pdftotext_ocr(os.path.join(upload_folder, filename)))
        else:
            extracted_text = (pdftotext(os.path.join(upload_folder, filename)))
            
        print(extracted_text)
        result.append(analyze_advertisement_img(extracted_text))
    return jsonify({'message': result})
