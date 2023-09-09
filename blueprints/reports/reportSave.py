from flask import Blueprint, request, jsonify, make_response, current_app, send_file
from io import BytesIO  # Import BytesIO from the io module
from Database.report import saveReport,getReportById

reports_bp = Blueprint("reports", __name__)

@reports_bp.route('/upload-pdf', methods=['POST'])
def pdfReportSave():
    try:
        # Retrieve the PDF report from the request files
        pdf_report = request.files['pdf'].read()
        
        # Retrieve the userID from the form data
        userID = request.form['userID']
        title = request.form['title']
        
        # Call the saveReport function with the PDF report data and userID
        saveReport(pdf_report, userID, title)
        
        return jsonify({"message": "PDF report saved successfully"}), 200
    except Exception as e:
        print(str(e))
        return jsonify({"error": "Error saving PDF report"}), 500



@reports_bp.route('/view-pdf', methods=['GET'])
def viewPdf():
    report_id = request.args.get('ReportID')
    print(report_id)
    
    report_data = getReportById(report_id)
    if report_data is not None and 'report' in report_data:
        # Serve the PDF to the user
        pdf_bytes = report_data['report']
        pdf_stream = BytesIO(pdf_bytes)
        return send_file(pdf_stream, mimetype='application/pdf')
    else:
        return jsonify({"error": "PDF not found"}), 404
    
