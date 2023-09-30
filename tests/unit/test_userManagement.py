import pytest
from tests.conftest import test_db
from Database.userManagement import deleteUserById, getAllUsers, getUserByID


def test_deleteUserById(test_db):
    # Insert a test user into the database
    test_user = {"User_ID": "test_user_id",
                 "name": "Test User", "password": "test_password"}
    test_db.User.insert_one(test_user)

    # Call the deleteUserById function
    result = deleteUserById("test_user_id", test_db)

    # Check if the user was deleted
    assert result is True
    test_db.Report.delete_many({})

# Test getAllUsers function


def test_getAllUsers(test_db):
    # Insert test users into the database
    test_users = [
        {"User_ID": "user1", "name": "User 1", "password": "password1"},
        {"User_ID": "user2", "name": "User 2", "password": "password2"},
    ]
    test_db.User.insert_many(test_users)

    # Call the getAllUsers function
    users = getAllUsers(test_db)

    # Check if the number of retrieved users matches the number of inserted test users
    assert len(users) == len(test_users)
    test_db.Report.delete_many({})

# Test getUserByID function


def test_getUserByID(test_db):
    # Insert a test user into the database
    test_user = {"User_ID": "test_user_id",
                 "name": "Test User", "password": "test_password"}
    test_db.User.insert_one(test_user)

    # Call the getUserByID function to retrieve the test user
    user = getUserByID("test_user_id", test_db)

    # Check if the retrieved user matches the test user
    assert user["User_ID"] == "test_user_id"
    test_db.Report.delete_many({})
