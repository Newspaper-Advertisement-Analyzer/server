from flask import Flask, request, jsonify, make_response
from NLP.webscraping import scrape_article_data
from NLP.pdf_to_text import extract_text_from_image
from NLP.detailextract import analyze_advertisement
from Database.connecctor import add_advertisement
from Database.connecctor import get_all_advertisement
import threading
from NLP.webScaper import extract_article_text
from flask import Flask,make_response,send_from_directory

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
            "location": location,
            "category": category,
            "phone_numbers": contact_info["phone_numbers"],
            "email_addresses": contact_info["email_addresses"],
            "prices": prices
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


if __name__ == '__main__':
    app.run(debug=True)
