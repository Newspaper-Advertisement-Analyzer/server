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

load_dotenv('./.env')

username: str = os.getenv('DBUSERNAME')
password: str = os.getenv('PASSWORD')

client = MongoClient("mongodb+srv://"+username+":"+password+"@cluster0.lemvb4s.mongodb.net/")
db = client.Advizor

def saveReport(pdf_report, user_ID, title):
    try:
        # Create a new document in the 'reports' collection to store the PDF report
        report_data = {
            "UserID": user_ID,
            "Title": title,
            "report": pdf_report,
            "timestamp": datetime.datetime.now()
        }
        db.Report.insert_one(report_data)
    except Exception as e:
        # Handle any errors that occur during the save operation
        return jsonify({"error": str(e)}), 500

def getReportById(report_id):
    try:
        # Retrieve the PDF report from the 'reports' collection by its ObjectId
        report_data = db.Report.find_one({"_id": ObjectId(report_id)})
        return report_data
    except Exception as e:
        # Handle any errors that occur during PDF retrieval
        return None