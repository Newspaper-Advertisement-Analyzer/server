import pytest
from tests.conftest import test_db, client
from Database.userSignUp import add_user


def test_add_user(client, test_db):
    # Define test user data
    test_user = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "password123"
    }

    # Call the add_user function
    result = add_user(test_user["name"],
                      test_user["email"], test_user["password"])

    # Check if the user was successfully added
    assert result is True
