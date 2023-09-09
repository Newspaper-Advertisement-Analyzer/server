from flask import Blueprint, request, jsonify, make_response, current_app
from Database.landSale import getAverageLandPriceByTimePeriod
from Database.houseSale import getAverageHousePriceByTimePeriod

averageSale_bp = Blueprint("averageSale", __name__)

@averageSale_bp.route('/getAverageLandPrice', methods=['GET'])
def landSaleby_time():
    time_period = request.args.get('interval')
    district = request.args.get('district')
    data = getAverageLandPriceByTimePeriod(time_period,district)
    return jsonify(data)

@averageSale_bp.route('/getAverageHousePrice', methods=['GET'])
def houseSaleby_time():
    time_period = request.args.get('interval')
    district = request.args.get('district')
    print(time_period,district)
    data = getAverageHousePriceByTimePeriod(time_period,district)
    return jsonify(data)
