from flask import Blueprint, request, jsonify, make_response, current_app
from Database.houseSale import categorizeHousesaleByCity

houseSalebyCity_bp = Blueprint("houseSalebyCity", __name__)

@houseSalebyCity_bp.route('/gethouseSalebyCity', methods=['GET'])
def houseSalebyCity():
    data = categorizeHousesaleByCity()
    print(data)
    return(jsonify(data))