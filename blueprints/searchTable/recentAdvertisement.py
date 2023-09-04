from flask import Blueprint, request, jsonify, make_response, current_app
from bson.json_util import dumps
from Database.landSale import getRecentLandSaleAdvertisements
from Database.houseSale import getRecentHouseSaleAdvertisements
from Database.marriageproposal import getRecentMarriageProposals

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
        # Convert the BSON date to a string in a suitable format (e.g., ISO 8601)
        ad["Posted_Date"] = ad["Posted_Date"].strftime("%Y-%m-%dT%H:%M:%S")
    return dumps(data)