from flask import Blueprint, request, jsonify, make_response, current_app
from Database.landSale import getRecentLandSaleAdLocation
from Database.houseSale import getRecentHouseSaleAdLocation
from Database.marriageproposal import getRecentMarriagePropLocation

recentAdLocation_bp = Blueprint("recentAdLocation", __name__)

@recentAdLocation_bp.route('/getRecentAdLocation', methods=['GET'])
def recentAdvertisementLandSale():
    adType = request.args.get('adtype')
    duration = request.args.get('duration')
    if adType == "LandSale":
        data = getRecentLandSaleAdLocation(duration)
    elif adType == "HouseSale":
        data = getRecentHouseSaleAdLocation(duration)
    elif adType == "MarriageProp":
        data = getRecentMarriagePropLocation(duration)
    return jsonify(data)

