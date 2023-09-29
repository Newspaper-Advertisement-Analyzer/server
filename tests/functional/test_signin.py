import json
import pytest
from Database.userSignUp import add_user
from tests.conftest import test_db, client


def test_login_valid_user(client):
    # Create a test user
    add_user("Test User", "test@example.com", "password123")

    # Send a POST request to the login endpoint
    response = client.post(
        "/login",
        data=json.dumps({"email": "test@example.com",
                        "password": "password123"}),
        content_type="application/json",
    )

    data = json.loads(response.data.decode("utf-8"))

    assert response.status_code == 200
    assert "message" in data
    assert "user" in data


def test_login_invalid_user(client):
    # Try to log in with invalid credentials
    response = client.post(
        "/login",
        data=json.dumps({"email": "invalid@example.com",
                        "password": "wrongpassword"}),
        content_type="application/json",
    )

    data = json.loads(response.data.decode("utf-8"))

    assert response.status_code == 401
    assert "error" in data
