from flask import Blueprint, request, jsonify, make_response, current_app
from Database.landSale import getAveragePricebyWeek

landSale_bp = Blueprint("landSale", __name__)

@landSale_bp.route('/getAverageLandPrice', methods=['GET'])
def landSalebytime():
    data = getAveragePricebyWeek()
    return(jsonify(data))

