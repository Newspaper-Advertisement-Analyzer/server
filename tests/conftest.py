import pytest
from pymongo import MongoClient
from app import create_app


@pytest.fixture(autouse=True)
def test_db():
    # Connect to a test database (you may need to use a different database name)
    client = MongoClient(
        "mongodb+srv://nadun:nadun2001@cluster0.lemvb4s.mongodb.net/")
    test_db = client.TestNewspaperAdAnalyzer

    yield test_db

    # Clean up after tests
    test_db.User.delete_many({})


@pytest.fixture(autouse=True)
def app(test_db):
    # Use the test database for the Flask app
    app = create_app(config={"TESTING": True})

    # Set the FLASK_ENV environment variable to "testing"
    app.config["ENV"] = "testing"

    yield app


@pytest.fixture(autouse=True)
def client(app):
    client = app.test_client()

    yield client
