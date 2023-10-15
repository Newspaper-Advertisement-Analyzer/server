import pytest
from datetime import datetime, timedelta
from tests.conftest import test_db
from Database.landSale import (
    getAverageLandPriceByTimePeriod,
    countLandsale,
    getRecentLandSaleAdvertisements,
    getRecentLandSaleAdLocation,
    getLatestLandSaleAd,
)


def test_getAverageLandPriceByTimePeriod(test_db):
    # Add test data to the database
    # ...

    # Call the function and make assertions
    result = getAverageLandPriceByTimePeriod("Weekly", "District")
    assert isinstance(result, list)
    # Add more assertions


def test_countLandsale(test_db):
    # Add test data to the database
    # ...

    # Call the function and make assertions
    result = countLandsale()
    assert isinstance(result, int)
    # Add more assertions


def test_getRecentLandSaleAdvertisements(test_db):
    # Add test data to the database
    # ...

    # Call the function and make assertions
    result = getRecentLandSaleAdvertisements()
    assert isinstance(result, list)
    # Add more assertions


def test_getRecentLandSaleAdLocation(test_db):
    # Add test data to the database
    # ...

    # Call the function and make assertions
    result = getRecentLandSaleAdLocation("Today")
    assert isinstance(result, list)
    # Add more assertions


def test_getLatestLandSaleAd(test_db):
    # Add test data to the database
    # ...

    # Call the function and make assertions
    result = getAverageLandPriceByTimePeriod("Weekly", "District")
    result_list = list(result)  # Convert the cursor to a list of dictionaries
    assert isinstance(result_list, list)
    # Add more assertions on the result_list
