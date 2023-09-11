from flask import Blueprint, request, jsonify, make_response, current_app, send_file
from io import BytesIO
from bson.json_util import dumps
from Database.report import saveReport, getReports
import json  # Import the json module to use json.dumps

getreports_bp = Blueprint("getreports", __name__)

@getreports_bp.route('/get-all-reports', methods=['GET'])
def getAllReports():
    # Call the getReports function to retrieve all reports
    reports = getReports()
    for report in reports:
        # Convert the BSON date to a string in a suitable format (e.g., ISO 8601)
        report["timestamp"] = report["timestamp"].strftime("%Y-%m-%dT%H:%M:%S")
    return dumps(reports)
