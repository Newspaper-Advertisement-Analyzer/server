from NLP import pdf_to_text


def test_extract_text_from_image():
    # Replace the path with a valid path to an image file in your project directory
    image_path = "uploadsimg\WhatsApp_Image_2023-09-13_at_09.46.31.jpg"
    extracted_text = pdf_to_text.extract_text_from_image(image_path)

    assert isinstance(extracted_text, str)

    # Add more assertions based on the expected behavior of the 'extract_text_from_image' function


def test_pdftotext():
    # Replace the path with a valid path to a PDF file in your project directory
    pdf_path = "uploadspdf\sample1.pdf"
    text = pdf_to_text.pdftotext(pdf_path)

    assert isinstance(text, str)

    # Add more assertions based on the expected behavior of the 'pdftotext' function


def test_pdftotext_ocr():
    # Replace the path with a valid path to a PDF file in your project directory
    pdf_path = "uploadspdf\sample1.pdf"
    text = pdf_to_text.pdftotext_ocr(pdf_path)

    assert isinstance(text, str)

    # Add more assertions based on the expected behavior of the 'pdftotext_ocr' function
