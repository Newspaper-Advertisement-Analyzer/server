import json
import pytest
from tests.conftest import client


def test_members_route_with_valid_data(client):
    # Replace this with an actual URL
    url = "https://www.hitad.lk/en/ad/1779332-Kalubowila-House-for-Sale?type=houses"
    data = {
        "inp": url
    }
    response = client.post("/members", json=data)
    assert response.status_code == 200
    # Add more assertions based on the expected behavior of the 'members' route


def test_members_route_with_invalid_data(client):
    invalid_data = {
        # Add invalid data or no 'inp' key to simulate an error
    }
    response = client.post("/members", json=invalid_data)
    assert response.status_code == 200  # or 400, depending on your error handling
    # Add more assertions based on the expected behavior of the 'members' route
