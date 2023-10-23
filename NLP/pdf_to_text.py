import pytesseract
from PIL import Image
import PyPDF2
import fitz  # PyMuPDF


def pdftotext(path):

    data = open(path, 'rb')
    reader = PyPDF2.PdfReader(data)
    print(len(reader.pages))
    text = ""
    # creating a page object
    for page in range(len(reader.pages)):
        page = reader.pages[page]
    # extracting text from page
        text += page.extract_text()
        text += "\n"
    # closing the pdf file object
    data.close()

    return text


def pdftotext_ocr(pdf_path):
    text = ""

    pdf_document = fitz.open(pdf_path)

    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        pix = page.get_pixmap()

        # Convert the pixmap to a PIL (Pillow) image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Perform OCR on the image
        page_text = pytesseract.image_to_string(img)

        text += page_text
        text += "\n"

    pdf_document.close()
    return text
