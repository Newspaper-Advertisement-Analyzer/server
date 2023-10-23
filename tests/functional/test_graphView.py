import json
import pytest
from tests.conftest import client


def test_ad_distribution(client):
    response = client.get('/adDistribution')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)  # Ensure that the response data is a list

    # Assuming that the function returns three elements in the list, each containing the count for different categories
    assert len(data) == 3

    # Ensure that each element in the list has the required structure
    expected_structure = {"label": str, "count": int}
    for item in data:
        assert all(key in item for key in expected_structure)

    # Add more assertions based on the expected behavior of the 'adDistribution' function


def test_get_average_land_price(client):
    response = client.get(
        '/getAverageLandPrice?interval=monthly&district=example_district')
    assert response.status_code == 200
    data = json.loads(response.data)
    # Add more assertions based on the expected behavior of the 'getAverageLandPrice' function


def test_get_average_house_price(client):
    response = client.get(
        '/getAverageHousePrice?interval=monthly&district=example_district')
    assert response.status_code == 200
    data = json.loads(response.data)
    # Add more assertions based on the expected behavior of the 'getAverageHousePrice' function


def test_house_sale_by_city(client):
    response = client.get('/gethouseSalebyCity')
    assert response.status_code == 200
    data = json.loads(response.data)
    # Add more assertions based on the expected behavior of the 'houseSalebyCity' function


def test_categorize_by_age(client):
    response = client.get('/categorizeby?criteria=Age')
    assert response.status_code == 200
    data = json.loads(response.data)
    # Add more assertions based on the expected behavior of the 'categorizebyAge' function


def test_categorize_by_profession(client):
    response = client.get('/categorizeby?criteria=Profession')
    assert response.status_code == 200
    data = json.loads(response.data)
    # Add more assertions based on the expected behavior of the 'categorizebyAge' function


def test_categorize_by_city(client):
    response = client.get('/categorizeby?criteria=District')
    assert response.status_code == 200
    data = json.loads(response.data)
    # Add more assertions based on the expected behavior of the 'categorizebyAge' function
