from flask import Blueprint, request, jsonify, make_response, current_app
from Database.landSale import getAveragePricebyWeek, getAveragePricebyMonth, getAveragePricebyYear

landSale_bp = Blueprint("landSale", __name__)

@landSale_bp.route('/getAverageLandPriceWeekly', methods=['GET'])
def landSalebytime_weekly():
    data = getAveragePricebyWeek()
    return jsonify(data)

@landSale_bp.route('/getAverageLandPriceMonthly', methods=['GET'])
def landSalebytime_monthly():
    data = getAveragePricebyMonth()
    return jsonify(data)

@landSale_bp.route('/getAverageLandPriceYearly', methods=['GET'])
def landSalebytime_yearly():
    data = getAveragePricebyYear()
    return jsonify(data)


