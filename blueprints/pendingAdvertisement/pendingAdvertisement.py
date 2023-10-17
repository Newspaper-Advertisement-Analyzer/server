from flask import Blueprint, request, jsonify
from Database.pendingAdvertisement import getAllPendingAds

getPendingAdvertisement_bp = Blueprint("getPendingAdvertisement", __name__)


@getPendingAdvertisement_bp.route('/pendingAdvertisements', methods=['GET'])
def get_all_pending_advertisements():
    try:
        ads = list(getAllPendingAds())
        return jsonify(ads)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
