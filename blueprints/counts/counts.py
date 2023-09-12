from flask import Blueprint, request, jsonify, make_response, current_app
from bson.json_util import dumps
from Database.userSignUp import countUers
from Database.landSale import countLandsale
from Database.houseSale import countHousesale
from Database.marriageproposal import countMarriageProposals
from Database.report import countReports

counts_bp = Blueprint("counts", __name__)

@counts_bp.route('/getcounts', methods=['GET'])
def databaseCount():
    houseSale_count = countHousesale()
    landeSale_count = countLandsale()
    prop_count = countMarriageProposals()

    data = {"user_count" :countUers(), 
    "ad_count":houseSale_count+ landeSale_count + prop_count,
    "report_count": countReports()}
    print(data)
    return jsonify(data)


