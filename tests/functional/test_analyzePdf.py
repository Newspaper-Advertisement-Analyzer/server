import json
import pytest
from tests.conftest import client


def test_upload_pdf_route_with_valid_pdf(client):
    # Replace the path with a valid path to a PDF file in your project directory
    with open(r"F:\Semester 5\Software Engineering Project\Project\server\uploadspdf\sample1.pdf", "rb") as pdf_file:
        data = {
            "pdfs": [pdf_file]
        }
        response = client.post("/uploadpdf", data=data,
                               content_type='multipart/form-data')
        assert response.status_code == 200
        # Add more assertions based on the expected behavior of the 'upload_pdf' route


def test_upload_pdf_route_with_invalid_pdf_type(client):
    # Replace the path with a valid path to a text file or any other non-PDF file
    with open("uploadsimg\WhatsApp_Image_2023-09-13_at_09.46.32.jpg", "rb") as pdf_file:
        data = {
            "pdfs": [pdf_file]
        }
        response = client.post("/uploadpdf", data=data,
                               content_type='multipart/form-data')
        assert response.status_code == 200  # or 400, depending on your error handling
        # Add more assertions based on the expected behavior of the 'upload_pdf' route


def test_upload_pdf_route_with_no_pdfs(client):
    data = {}
    response = client.post("/uploadpdf", data=data)
    assert response.status_code == 200  # or 400, depending on your error handling
    # Add more assertions based on the expected behavior of the 'upload_pdf' route
