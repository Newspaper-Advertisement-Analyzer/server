import pytest
import datetime
from bson import ObjectId
from tests.conftest import test_db
from Database.report import (
    saveReport,
    getReportById,
    getReports,
    countReports,
)
from flask import appcontext_pushed, g

# Your test_saveReport function


def test_saveReport(test_db, app):
    # Create a Flask app context within the test function
    with app.app_context():
        # Call the function to save a report
        response, status_code = saveReport(
            "sample_pdf_url", "user123", "Sample Report", test_db)

        # Assert that the response status code is 200, indicating success
        assert status_code == 200

        # Retrieve the saved report from the test database and assert its existence
        saved_report = test_db.Report.find_one({"PDF_URL": "sample_pdf_url"})
        assert saved_report is not None

        # Clean up: Delete the saved report from the database
        test_db.Report.delete_one({"PDF_URL": "sample_pdf_url"})

# Test getReportById function


def test_getReportById(test_db):
    # Create a sample report and add it to the test database
    sample_report = {
        "UserID": "user123",
        "Title": "Sample Report",
        "PDF_URL": "sample_pdf_url",
        "timestamp": datetime.datetime.now()
    }
    report_id = test_db.Report.insert_one(sample_report).inserted_id

    # Call the function to retrieve the report by its ID
    retrieved_report = getReportById(str(report_id), test_db)

    # Assert that the retrieved report matches the sample report
    assert retrieved_report["UserID"] == sample_report["UserID"]
    assert retrieved_report["Title"] == sample_report["Title"]

    test_db.Report.delete_many({})


def test_getReports(test_db):
    # Create sample reports and add them to the test database
    sample_reports = [
        {
            "UserID": "user123",
            "Title": "Report 1",
            "PDF_URL": "pdf_url_1",
            "timestamp": datetime.datetime.now()
        },
        {
            "UserID": "user456",
            "Title": "Report 2",
            "PDF_URL": "pdf_url_2",
            "timestamp": datetime.datetime.now()
        },
    ]
    report_ids = [str(test_db.Report.insert_one(report).inserted_id)
                  for report in sample_reports]

    # Call the function to retrieve all reports
    retrieved_reports = getReports(test_db)

    # Assert that the number of retrieved reports matches the number of sample reports
    assert len(retrieved_reports) == len(sample_reports)

    # Clean up: Delete the sample reports from the database
    for report_id in report_ids:
        test_db.Report.delete_one({"_id": ObjectId(report_id)})

# Test countReports function


def test_countReports(test_db):
    # Create sample reports and add them to the test database
    sample_reports = [
        {
            "UserID": "user123",
            "Title": "Report 1",
            "PDF_URL": "pdf_url_1",
            "timestamp": datetime.datetime.now()
        },
        {
            "UserID": "user456",
            "Title": "Report 2",
            "PDF_URL": "pdf_url_2",
            "timestamp": datetime.datetime.now()
        },
    ]
    [test_db.Report.insert_one(report) for report in sample_reports]

    # Call the function to count the number of reports
    report_count = countReports(test_db)

    # Assert that the report count matches the number of sample reports
    assert report_count == len(sample_reports)

    # Clean up: Delete the sample reports from the database
    test_db.Report.delete_many({})
