from flask import Blueprint, request, jsonify, make_response, current_app
from Database.landSale import getRecentLandSaleAdLocation
from Database.houseSale import getRecentHouseSaleAdLocation
from Database.marriageproposal import getRecentMarriagePropLocation
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
import datetime
import os
from Database.db_connector import db


def saveReport(pdf_url, user_ID, title, dbName=db):
    try:
        # Create a new document in the 'reports' collection to store the PDF URL
        report_data = {
            "UserID": user_ID,
            "Title": title,
            "PDF_URL": pdf_url,  # Save the PDF URL
            "timestamp": datetime.datetime.now()
        }

        # Assuming you have a 'reports' collection in your database
        # Update the collection name as needed
        dbName.Report.insert_one(report_data)

        return jsonify({"message": "Report saved successfully"}), 200
    except Exception as e:
        # Handle any errors that occur during the save operation
        return jsonify({"error": str(e)}), 500


def getReportById(report_id, dbName=db):
    try:
        # Retrieve the PDF report from the 'reports' collection by its ObjectId
        report_data = dbName.Report.find_one({"_id": ObjectId(report_id)})
        return report_data
    except Exception as e:
        # Handle any errors that occur during PDF retrieval
        return None


def getReports(userID, dbName=db):
    try:
        # Retrieve reports for the specified userID from the 'reports' collection
        reports = list(dbName.Report.find({"UserID": userID}, {"_id": 0}))

        # Optionally, convert the BSON date to a string in a suitable format (e.g., ISO 8601)
        for report in reports:
            report["timestamp"] = report["timestamp"].strftime(
                "%Y-%m-%dT%H:%M:%S")
        print(reports)
        return reports
    except Exception as e:
        # Handle any errors that occur during retrieval
        return None


def countReports(dbName=db):
    count = dbName.Report.count_documents({})
    return count
