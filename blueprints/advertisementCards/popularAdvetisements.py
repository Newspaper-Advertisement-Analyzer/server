from flask import Blueprint, jsonify
from Database.landSale import getLatestLandSaleAd
from Database.houseSale import getLatestHouseSaleAd
from Database.marriageproposal import getLatestMarriageProposalSaleAd

popularAd_bp = Blueprint("popularAd", __name__)

@popularAd_bp.route('/getPopularAd', methods=['GET'])
def getPopularAds():
    land_sale_ad = getLatestLandSaleAd()
    house_sale_ad = getLatestHouseSaleAd()
    marriage_proposal_ad = getLatestMarriageProposalSaleAd()

    # Add category to each advertisement and reformat the data
    categorized_ads = []
    for ad_data, category in [(land_sale_ad, "Land Sale"), (house_sale_ad, "House Sale"), (marriage_proposal_ad, "Marriage Proposal")]:
        for ad in ad_data:
            categorized_ads.append({"Advertisement_ID": ad["Advertisement_ID"], "category": category, "Title": ad["Title"], "Description": ad["Description"]})
    print(categorized_ads)
    return jsonify(categorized_ads)
 