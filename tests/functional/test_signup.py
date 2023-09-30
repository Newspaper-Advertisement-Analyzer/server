import json
import pytest
from Database.userSignUp import add_user
from tests.conftest import test_db, client


def test_signup(client):
    # Define test data for the /signup route
    test_data = {
        "name": "verify User",
        "email": "verify@example.com",
        "password": "password123"
    }

    # Send a POST request to the /signup route
    response = client.post("/signup", json=test_data)

    # Check if the response status code is 200 OK (successful request)
    assert response.status_code == 200

    # Parse the JSON response
    data = json.loads(response.data)

    # Check if the response message is as expected
    assert data["message"] == "Verification code sent."


def test_verify(client):
    # Define test data for the /verify route
    test_data = {
        "email": "verify@example.com",
        "verificationCode": "123456"
    }

    # Send a POST request to the /verify route
    response = client.post("/verify", json=test_data)

    # Check if the response status code is 200 OK (successful request)
    assert response.status_code == 200

    # Parse the JSON response
    data = json.loads(response.data)

    # Check if the "success" key in the response is True (verification successful)
    assert data["success"] is True
