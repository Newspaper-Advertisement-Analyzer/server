from flask import Blueprint, request, jsonify, make_response, current_app
from Database.landSale import getRecentLandSaleAdLocation
from Database.houseSale import getRecentHouseSaleAdLocation
from Database.marriageproposal import getRecentMarriagePropLocation

recentAdLocation_bp = Blueprint("recentAdLocation", __name__)

@recentAdLocation_bp.route('/getRecentAdLocationLandSale', methods=['GET'])
def recentAdvertisementLandSale():
    data = getRecentLandSaleAdLocation()
    return jsonify(data)

@recentAdLocation_bp.route('/getRecentAdLocationHouseSale', methods=['GET'])
def recentAdvertisementHouseSale():
    data = getRecentHouseSaleAdLocation()
    return jsonify(data)

@recentAdLocation_bp.route('/getRecentAdLocationMarriageProp', methods=['GET'])
def recentAdvertisementMarriageProp():
    data = getRecentMarriagePropLocation()
    return data