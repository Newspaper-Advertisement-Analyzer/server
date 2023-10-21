# import pytesseract
# from PIL import Image
# import PyPDF2
# import fitz  # PyMuPDF


# def extract_text_from_image(image_path):
#     # Perform text extraction using Tesseract
#     extracted_text = pytesseract.image_to_string(Image.open(image_path))
#     return extracted_text


# # creating a pdf file object

# def pdftotext(path):

#     data = open(path, 'rb')
#     # creating a pdf reader object
#     reader = PyPDF2.PdfReader(data)
#     # printing number of pages in pdf file
#     print(len(reader.pages))
#     text = ""
#     # creating a page object
#     for page in range(len(reader.pages)):
#         page = reader.pages[page]
#     # extracting text from page
#         text += page.extract_text()
#         text += "\n"
#     # closing the pdf file object
#     data.close()

#     return text


# def pdftotext_ocr(pdf_path):
#     text = ""

#     pdf_document = fitz.open(pdf_path)

#     for page_number in range(len(pdf_document)):
#         page = pdf_document[page_number]
#         pix = page.get_pixmap()

#         # Convert the pixmap to a PIL (Pillow) image
#         img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

#         # Perform OCR on the image
#         page_text = pytesseract.image_to_string(img)

#         text += page_text
#         text += "\n"

#     pdf_document.close()
#     return text
import pytesseract
from pdfplumber import open
from PIL import Image, ImageEnhance, ImageFilter
import io


def preprocess_image(image):
    # Convert the PageImage object to bytes
    with io.BytesIO() as output:
        image.save(output, format='PNG')
        contents = output.getvalue()
    pil_image = Image.open(io.BytesIO(contents))

    # Enhance image for better OCR results
    pil_image = pil_image.convert("L")  # Convert to grayscale
    pil_image = ImageEnhance.Contrast(
        pil_image).enhance(2)  # Increase contrast
    # Apply median filter to reduce noise
    pil_image = pil_image.filter(ImageFilter.MedianFilter())
    return pil_image


def extract_text_from_image(image_path):
    img = Image.open(image_path)
    processed_img = preprocess_image(img)
    # Perform text extraction using Tesseract
    extracted_text = pytesseract.image_to_string(processed_img)
    return extracted_text


def pdftotext(path):
    text = ""
    with open(path) as pdf:
        pages = pdf.pages
        for page in pages:
            text += page.extract_text()
    return text


def pdftotext_ocr(pdf_path):
    text = ""
    with open(pdf_path) as pdf:
        pages = pdf.pages
        for page in pages:
            im = page.to_image()
            processed_img = preprocess_image(im)
            extracted_text = pytesseract.image_to_string(processed_img)
            text += extracted_text
            text += "\n"
    return text
