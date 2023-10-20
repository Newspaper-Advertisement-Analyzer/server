from flask import Blueprint, request, jsonify, make_response, current_app
from bson.json_util import dumps
from Database.landSale import getRecentLandSaleAdvertisements
from Database.houseSale import getRecentHouseSaleAdvertisements
from Database.marriageproposal import getRecentMarriageProposals
from datetime import datetime

recentAd_bp = Blueprint("recentAd", __name__)


@recentAd_bp.route('/getRecentAdLandSale', methods=['GET'])
def recentAdvertisementLandSale():
    data = getRecentLandSaleAdvertisements()
    return jsonify(data)


@recentAd_bp.route('/getRecentAdHouseSale', methods=['GET'])
def recentAdvertisementHouseSale():
    data = getRecentHouseSaleAdvertisements()
    return jsonify(data)


@recentAd_bp.route('/getRecentAdMarriageProp', methods=['GET'])
def recentAdvertisementMarriageProp():
    data = getRecentMarriageProposals()
    for ad in data:
        # Check if ad["Posted_Date"] is a string and convert it to a datetime object
        if isinstance(ad["Posted_Date"], str):
            # or use datetime.strptime if the format is different
            ad["Posted_Date"] = datetime.fromisoformat(ad["Posted_Date"])

        # Convert the date to the desired string format
        ad["Posted_Date"] = ad["Posted_Date"].strftime("%Y-%m-%dT%H:%M:%S")
    return dumps(data)
