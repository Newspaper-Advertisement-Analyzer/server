import pytesseract
from PIL import Image

def extract_text_from_image(image_path):
    # Perform text extraction using Tesseract
    extracted_text = pytesseract.image_to_string(Image.open(image_path))
    return extracted_text
