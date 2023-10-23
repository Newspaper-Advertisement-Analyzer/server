import pytest
from datetime import datetime, timedelta
from tests.conftest import test_db
from Database.houseSale import (
    getAverageHousePriceByTimePeriod,
    countHousesale,
    categorizeHousesaleByCity,
    getRecentHouseSaleAdvertisements,
    getRecentHouseSaleAdLocation,
    getLatestHouseSaleAd,
)


def test_getAverageHousePriceByTimePeriod(test_db):
    # Add test data to the database
    # ...

    # Call the function and make assertions
    result = getAverageHousePriceByTimePeriod("Weekly", "District")
    assert isinstance(result, list)
    # Add more assertions


def test_countHousesale(test_db):
    # Add test data to the database
    # ...

    # Call the function and make assertions
    result = countHousesale()
    assert isinstance(result, int)
    # Add more assertions


def test_categorizeHousesaleByCity(test_db):
    # Add test data to the database
    # ...

    # Call the function and make assertions
    result = categorizeHousesaleByCity()
    assert isinstance(result, list)
    # Add more assertions


def test_getRecentHouseSaleAdvertisements(test_db):
    # Add test data to the database
    # ...

    # Call the function and make assertions
    result = getRecentHouseSaleAdvertisements()
    assert isinstance(result, list)
    # Add more assertions


def test_getRecentHouseSaleAdLocation(test_db):
    # Add test data to the database
    # ...

    # Call the function and make assertions
    result = getRecentHouseSaleAdLocation("Today")
    assert isinstance(result, list)
    # Add more assertions


def test_getLatestHouseSaleAd(test_db):
    # Add test data to the database
    # ...

    # Call the function and make assertions
    result = getLatestHouseSaleAd()
    result_list = list(result)  # Convert the cursor to a list of dictionaries
    assert isinstance(result_list, list)
    # Add more assertions
