import json
import pytest
from tests.conftest import client


def test_recent_ad_land_sale(client):
    response = client.get('/getRecentAdLandSale')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)  # Ensure that the response data is a list
    # Add more assertions based on the expected behavior of the 'recentAdvertisementLandSale' function


def test_recent_ad_house_sale(client):
    response = client.get('/getRecentAdHouseSale')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)  # Ensure that the response data is a list
    # Add more assertions based on the expected behavior of the 'recentAdvertisementHouseSale' function


def test_recent_ad_marriage_prop(client):
    response = client.get('/getRecentAdMarriageProp')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)  # Ensure that the response data is a list
    # Add more assertions based on the expected behavior of the 'recentAdvertisementMarriageProp' function
