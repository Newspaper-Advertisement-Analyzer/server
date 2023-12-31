from flask import Blueprint, request, jsonify
from Database.landSale import saveLandSaleAdvertisement
from Database.houseSale import saveHouseSaleAdvertisement
from Database.marriageproposal import saveMarriageProposalAdvertisement

advertisement_bp = Blueprint("advertisement", __name__)


@advertisement_bp.route('/submitAdvertisement', methods=['POST'])
def submit_advertisement():
    try:
        data = request.get_json()
        print(data)
        category = data.get("category")

        if category == "Land Sale":
            result = saveLandSaleAdvertisement(data.get("title"), data.get("location"), data.get("postedOn"),
                                               data.get("description"), data.get(
                                                   "image"), data.get("pricePerPerch"),
                                               data.get("numberOfPerches"), data.get(
                                                   "postedOn"), data.get("source"),
                                               data.get("phoneNumbers"), data.get(
                                                   "email"), data.get("nearestCity"),
                                               data.get("address"), data.get("landMarks"), data.get("longitude"), data.get("lattitude"))
        elif category == "House Sale":
            result = saveHouseSaleAdvertisement(data.get("title"), data.get("location"), data.get("postedOn"),
                                                data.get("description"), data.get(
                                                    "image"), data.get("price"),
                                                data.get("numberOfRooms"), data.get(
                                                    "postedOn"), data.get("source"),
                                                data.get("phoneNumbers"), data.get(
                                                    "email"), data.get("nearestCity"),
                                                data.get("address"), data.get("longitude"), data.get("lattitude"))
        elif category == "Marriage Proposals":
            result = saveMarriageProposalAdvertisement(data.get("title"), data.get("location"), data.get("postedOn"),
                                                       data.get("description"), data.get(
                                                           "image"), data.get("gender"),
                                                       data.get("age"), data.get(
                                                           "profession"), data.get("nationality"),
                                                       data.get("requirements"), data.get(
                                                           "postedOn"), data.get("source"),
                                                       data.get("phoneNumbers"), data.get(
                                                           "email"), data.get("nearestCity"),
                                                       data.get("address"), data.get("longitude"), data.get("lattitude"))

        if result:
            return jsonify({"message": "Advertisement saved successfully"})
        else:
            return jsonify({"error": "Failed to save advertisement"})
    except Exception as e:
        return jsonify({"error": str(e)})
