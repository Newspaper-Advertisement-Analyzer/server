import pytest
from datetime import datetime, timedelta
from tests.conftest import test_db
from Database.marriageproposal import (
    countMarriageProposals,
    categorizeMarriageProposalsByAge,
    categorizeMarriageProposalsByProfession,
    categorizeMarriageProposalsByCity,
    getRecentMarriageProposals,
    getRecentMarriagePropLocation,
    getLatestMarriageProposalSaleAd,
)

# Assuming you have a 'test_db' fixture and 'client' fixture

# Test countMarriageProposals function


def test_countMarriageProposals(test_db):
    # Add some test data to the 'Marriage_Proposal' collection in the test database
    # ...

    # Call the function and assert the result
    result = countMarriageProposals()
    assert isinstance(result, int)
    # Add more assertions if needed

# Test categorizeMarriageProposalsByAge function


def test_categorizeMarriageProposalsByAge(test_db):
    # Add some test data to the 'Marriage_Proposal' collection in the test database
    # ...

    # Call the function and assert the result
    result = categorizeMarriageProposalsByAge()
    assert isinstance(result, list)
    # Add more assertions if needed

# Test categorizeMarriageProposalsByProfession function


def test_categorizeMarriageProposalsByProfession(test_db):
    # Add some test data to the 'Marriage_Proposal' collection in the test database
    # ...

    # Call the function and assert the result
    result = categorizeMarriageProposalsByProfession()
    assert isinstance(result, list)
    # Add more assertions if needed

# Test categorizeMarriageProposalsByCity function


def test_categorizeMarriageProposalsByCity(test_db):
    # Add some test data to the 'Marriage_Proposal' collection in the test database
    # ...

    # Call the function and assert the result
    result = categorizeMarriageProposalsByCity()
    assert isinstance(result, list)
    # Add more assertions if needed

# Test getRecentMarriageProposals function


def test_getRecentMarriageProposals(test_db):
    # Add some test data to the 'Marriage_Proposal' collection in the test database
    # ...

    # Call the function and assert the result
    result = getRecentMarriageProposals()
    assert isinstance(result, list)
    # Add more assertions if needed

# Test getRecentMarriagePropLocation function


def test_getRecentMarriagePropLocation(test_db):
    # Add some test data to the 'Marriage_Proposal' collection in the test database
    # ...

    # Call the function with a duration and assert the result
    result = getRecentMarriagePropLocation("Today")
    assert isinstance(result, list)
    # Add more assertions if needed

# Test getLatestMarriageProposalSaleAd function


def test_getLatestMarriageProposalSaleAd(test_db):
    # Add some test data to the 'Marriage_Proposal' collection in the test database
    # ...

    # Call the function and assert the result
    result = getLatestMarriageProposalSaleAd()
    result_list = list(result)  # Convert the cursor to a list of dictionaries
    assert isinstance(result_list, list)
