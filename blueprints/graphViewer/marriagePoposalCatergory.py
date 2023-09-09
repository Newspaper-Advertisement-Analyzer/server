from flask import Blueprint, request, jsonify, make_response, current_app
from Database.marriageproposal import categorizeMarriageProposalsByAge, categorizeMarriageProposalsByProfession, categorizeMarriageProposalsByCity

categorizebyAge_bp = Blueprint("categorizeby", __name__)

@categorizebyAge_bp.route('/categorizeby', methods=['GET'])
def categorizebyAge():
    criteria = request.args.get('criteria')
    if criteria == "Age":
        data = categorizeMarriageProposalsByAge()
    elif criteria == "Profession":
        data = categorizeMarriageProposalsByProfession()
    elif criteria == "District":
        data = categorizeMarriageProposalsByCity()
    return(jsonify(data))