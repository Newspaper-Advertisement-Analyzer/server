import json
import pytest
from tests.conftest import client
from blueprints.searchBar.searchByFilters import convert_date_format


def test_search_recent_ads(client):
    response = client.get(
        '/filter-ads?selectedOption=Date&searchQuery=example_query&startDate=2023-10-01&endDate=2023-10-15&category=example_category')
    assert response.status_code == 200
    data = json.loads(response.data)
    # Add more assertions based on the expected behavior of the 'search_recent_ads' function


def test_convert_date_format():
    # Replace 'example_date_str' with a valid date string in the format "YYYY-MM-DD"
    example_date_str = '2023-10-01'
    formatted_date = convert_date_format(example_date_str)
    assert isinstance(formatted_date, str)  # Ensure the output is a string
    # Add more assertions based on the expected behavior of the 'convert_date_format' function
