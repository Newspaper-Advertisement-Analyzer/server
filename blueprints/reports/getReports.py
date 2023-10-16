from flask import Blueprint, request, jsonify, make_response, current_app, send_file
from io import BytesIO
from bson.json_util import dumps
from Database.report import saveReport, getReports
import json  # Import the json module to use json.dumps

getreports_bp = Blueprint("getreports", __name__)


@getreports_bp.route('/get-all-reports', methods=['POST'])
def getAllReports():
    try:
        data = request.get_json()
        userID = data.get('userID')
        if not userID:
            return jsonify({"error": "UserID is required"}), 400

        # Call the getReports function to retrieve reports for the specified userID
        reports = getReports(userID)
        if reports is not None:
            return dumps(reports)
        else:
            return jsonify({"error": "Error retrieving reports"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
