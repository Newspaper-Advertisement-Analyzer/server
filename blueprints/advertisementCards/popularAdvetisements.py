from flask import Blueprint, jsonify,  request
from Database.landSale import getLatestLandSaleAd
from Database.houseSale import getLatestHouseSaleAd
from Database.marriageproposal import getLatestMarriageProposalSaleAd
from Database.advertisementSearch import searchADbyID

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

    return jsonify(categorized_ads)


@popularAd_bp.route('/getAdDetails', methods=['GET'])
def searchAdDetails():
    adverisementID = request.args.get('adID')
    if adverisementID[2] == "1":
        data = searchADbyID(adverisementID, "HouseSale_Advertisement")
    elif adverisementID[2] == "2":
        data = searchADbyID(adverisementID, "LandSale_Advertisement")
    elif adverisementID[2] == "3":
        data = searchADbyID(adverisementID, "Marriage_Proposals")
    return jsonify(data)
    
 