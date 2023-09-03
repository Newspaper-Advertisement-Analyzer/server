from flask import Blueprint, request, jsonify, make_response, current_app
from Database.marriageproposal import categorizeMarriageProposalsByAge

categorizebyAge_bp = Blueprint("categorizebyAge", __name__)

@categorizebyAge_bp.route('/categorizebyAge', methods=['GET'])
def categorizebyAge():
    data = categorizeMarriageProposalsByAge()
    return(jsonify(data))