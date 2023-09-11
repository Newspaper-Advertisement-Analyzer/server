from flask import Blueprint, request, jsonify, make_response, current_app, send_file
from io import BytesIO  # Import BytesIO from the io module
from Database.report import saveReport,getReportById

getreports_bp = Blueprint("getreports", __name__)

@getreports_bp.route('/get-all-reports', methods=['GET'])
def getAllReports():
    try:
        # Call the getReports function to retrieve all reports
        reports = getReports()

        if reports is not None:
            # Convert the reports to JSON format
            reports_json = dumps(reports)
            return jsonify({"reports": reports_json})
        else:
            return jsonify({"error": "Error fetching reports"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
