import json
import pytest
from tests.conftest import client


def test_database_count(client):
    response = client.get('/getcounts')
    assert response.status_code == 200
    data = json.loads(response.data)
    # Ensure that the response data is a dictionary
    assert isinstance(data, dict)
    # Add more assertions based on the expected behavior of the 'databaseCount' function
    assert all(key in data for key in [
               'user_count', 'ad_count', 'report_count'])
    # Ensure that the user count is an integer
    assert isinstance(data['user_count'], int)
    # Ensure that the ad count is an integer
    assert isinstance(data['ad_count'], int)
    # Ensure that the report count is an integer
    assert isinstance(data['report_count'], int)
