import pytest
from tests.conftest import test_db, client
from Database.userSignUp import add_user, delete_user, countUers, validate_user, find_user

sample_user = {
    "name": "Test User",
    "email": "test@example.com",
    "password": "password123"
}


def test_add_user(client, test_db):
    # Define test user data
    test_user = {
        "name": "11",
        "email": "test@example.com",
        "password": "password123"
    }

    # Call the add_user function with the test database
    result = add_user(
        test_user["name"], test_user["email"], test_user["password"], test_db)

    # Check if the user was successfully added
    assert result is True


def test_delete_user(test_db):
    # Add a sample user to the database for deletion testing
    add_user(sample_user["name"], sample_user["email"],
             sample_user["password"], test_db)

    # Call the delete_user function to delete the sample user with the test database
    result = delete_user(sample_user["email"], test_db)

    # Check if the user was successfully deleted
    assert result is True

    # Check if the user no longer exists in the test database
    deleted_user = test_db.User.find_one({"email": sample_user["email"]})
    assert deleted_user is None


def test_find_user(test_db):
    # Add a sample user to the database for find_user testing
    add_user(sample_user["name"], sample_user["email"],
             sample_user["password"], test_db)

    # Call the find_user function to find the sample user with the test database
    found_user = find_user(sample_user["email"], test_db)

    # Check if the found_user is not None (i.e., user is found)
    assert found_user is not None


def test_validate_user(test_db):
    # Add a sample user to the database for validation testing
    add_user(sample_user["name"], sample_user["email"],
             sample_user["password"], test_db)

    # Call the validate_user function with correct password with the test database
    valid_user = validate_user(
        sample_user["email"], sample_user["password"], test_db)

    # Call the validate_user function with incorrect password with the test database
    invalid_user = validate_user(
        sample_user["email"], "wrongpassword", test_db)

    # Check if the valid_user is True (i.e., password is correct)
    assert valid_user is True

    # Check if the invalid_user is False (i.e., password is incorrect)
    assert invalid_user is False


def test_count_users(test_db):
    # Add multiple sample users to the database for counting testing with the test database
    add_user("User1", "user1@example.com", "password1", test_db)
    add_user("User2", "user2@example.com", "password2", test_db)
    add_user("User3", "user3@example.com", "password3", test_db)

    # Call the countUers function to count the number of users with the test database
    user_count = countUers(test_db)

    # Check if the user_count is equal to the number of added users
    assert user_count == 3  # Including the sample_user added earlier
