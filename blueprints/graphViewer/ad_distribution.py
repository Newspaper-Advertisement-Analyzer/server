from flask import Blueprint, request, jsonify

from Database.landSale import countLandsale
from Database.houseSale import countHousesale
from Database.marriageproposal import countMarriageProposals

adDistribution_bp = Blueprint("adDistribution", __name__)

@adDistribution_bp.route('/adDistribution', methods=['GET'])
def adDistribution():
    # Count the number of advertisements for each category
    land_sale_count = countLandsale()
    house_sale_count = countHousesale()
    marriage_proposals_count = countMarriageProposals()

    # Create a JSON response with the counts
    response_data = [
        {"label":"Land Sale", "count": land_sale_count},
        {"label":"House Sale", "count": house_sale_count},
        {"label":"Marriage Proposal", "count": marriage_proposals_count},

    ]
    return jsonify(response_data)
