import pytest
from mongomock import MongoClient
from Database.userSignUp import add_user, delete_user, find_user, validate_user

# Use mongomock for testing
@pytest.fixture
def mock_db():
    # Create a mongomock client and return it
    return MongoClient().db

def test_add_user(mock_db):
    # Arrange
    name = "Test User"
    email = "test@example.com"
    password = "password"

    # Act
    result = add_user(mock_db, name, email, password)

    # Assert
    assert result is True
    user = mock_db.user.find_one({"email": email})
    assert user is not None
    assert user["name"] == name
    assert user["email"] == email

def test_delete_user(mock_db):
    # Arrange
    email = "test@example.com"
    mock_db.user.insert_one({"email": email})

    # Act
    result = delete_user(mock_db, email)

    # Assert
    assert result is True
    user = mock_db.user.find_one({"email": email})
    assert user is None

def test_find_user(mock_db):
    # Arrange
    email = "test@example.com"
    mock_db.user.insert_one({"email": email})

    # Act
    user = find_user(mock_db, email)

    # Assert
    assert user is not None
    assert user["email"] == email

def test_validate_user(mock_db):
    # Arrange
    email = "test@example.com"
    password = "password"
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    mock_db.user.insert_one({"email": email, "password": hashed_password})

    # Act and Assert
    assert validate_user(mock_db, email, password) is True
    assert validate_user(mock_db, email, "wrong_password") is False
    assert validate_user(mock_db, "nonexistent@example.com", password) is False
