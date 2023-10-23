import json
import pytest
from tests.conftest import client


def test_get_all_reports(client):
    response = client.get('/get-all-reports')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)  # Ensure the response data is a list
    # Add more assertions based on the expected behavior of the 'getAllReports' function


def test_pdf_report_save(client):
    data = {
        'pdfURL': 'example_pdf_url',
        'userID': 'example_user_id',
        'title': 'example_title'
    }
    response = client.post('/upload-pdf-url', data=data)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['message'] == "PDF URL saved successfully"
    # Add more assertions based on the expected behavior of the 'pdfReportSave' function


def test_view_pdf(client):
    # Replace 'example_report_id' with a valid report ID
    report_id = 'example_report_id'
    response = client.get(f'/view-pdf?ReportID={report_id}')
    assert response.status_code == 404  # or 404, depending on your error handling
    # Add more assertions based on the expected behavior of the 'viewPdf' function
