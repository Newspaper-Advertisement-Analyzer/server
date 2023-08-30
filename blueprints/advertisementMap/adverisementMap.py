from flask import Blueprint, jsonify
from Database.adCollection import get_all_advertisement

advertisementsMap_bp = Blueprint("advertisementMap", __name__)

@advertisementsMap_bp.route("/get_marker_locations", methods=['GET'])
def get_markers():
    markers = get_all_advertisement()
    return jsonify(markers)
