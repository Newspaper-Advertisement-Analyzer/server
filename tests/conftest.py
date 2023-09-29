import pytest
from pymongo import MongoClient
from main import create_app


@pytest.fixture(scope="module")
def test_db():
    # Connect to a test database (you may need to use a different database name)
    client = MongoClient(
        "mongodb+srv://nadun:nadun2001@cluster0.lemvb4s.mongodb.net/")
    test_db = client.TestNewspaperAdAnalyzer

    yield test_db

    # Clean up after tests
    test_db.User.delete_many({})


@pytest.fixture
def client():
    # Use the test database for the Flask app
    app = create_app(config={"TESTING": True})
    client = app.test_client()

    yield client
