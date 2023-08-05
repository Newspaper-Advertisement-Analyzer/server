from flask import Flask, request, jsonify, make_response
from NLP.webscraping import scrape_article_data
from NLP.pdf_to_text import extract_text_from_image
from NLP.detailextract import analyze_advertisement
from Database.connecctor import add_advertisement
from Database.connecctor import get_all_advertisement
import threading

app = Flask(__name__)

@app.route('/members', methods=['POST'])
def members():
    inp = request.json.get("inp")
    print(inp)
    try:
        article_data = scrape_article_data(inp)
        location, category, contact_info, prices = analyze_advertisement(article_data)
        ad_data = {
            "location": location,
            "category": category,
            "phone_numbers": contact_info["phone_numbers"],
            "email_addresses": contact_info["email_addresses"],
            "prices": prices
        }
        
        # Create a new thread for the add_advertisement function
        thread = threading.Thread(target=add_advertisement, args=(ad_data,))
        thread.start()

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


if __name__ == '__main__':
    app.run(debug=True)
