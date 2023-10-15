import json
import pytest
from tests.conftest import client


def test_process_image_route_with_valid_image(client):
    # Replace the path with a valid path to an image file in your project directory
    with open(r"F:\Semester 5\Software Engineering Project\Project\server\uploadsimg\WhatsApp_Image_2023-09-13_at_09.46.31.jpg", "rb") as image_file:
        data = {
            "image": (image_file, "image.png")
        }
        response = client.post("/process_image", data=data,
                               content_type='multipart/form-data')
        assert response.status_code == 200
        # Add more assertions based on the expected behavior of the 'process_image' route


def test_process_image_route_with_no_image(client):
    data = {}
    response = client.post("/process_image", data=data)
    assert response.status_code == 200  # or 400, depending on your error handling
    # Add more assertions based on the expected behavior of the 'process_image' route
