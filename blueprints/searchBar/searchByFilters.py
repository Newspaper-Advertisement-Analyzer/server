from flask import Blueprint, request, jsonify, make_response, current_app
from bson.json_util import dumps
from Database.advertisementSearch import search_ads_by_filters


searchByFilters_bp = Blueprint("searchByFilters", __name__)

@searchByFilters_bp.route('/recent-ads', methods=['GET'])
def search_recent_ads():
    selected_option = request.args.get('selectedOption')
    search_query = request.args.get('searchQuery')
    print(selected_option,search_query)
    if not selected_option or not search_query:
        return jsonify({"error": "Missing search criteria"}), 400

    if selected_option == "Date":
        # Implement your logic to search by date
        #data = search_ads_by_filters(search_query)
        pass
    elif selected_option == "Category":
        # Implement your logic to search by category
        pass
    elif selected_option == "Location":
        # Implement your logic to search by location
        pass
    elif selected_option == "Title":
        # Implement your logic to search by title
        pass
    else:
        return jsonify({"error": "Invalid selectedOption"}), 400

    # Return the search results (modify this as needed)
    return jsonify(data)

# You can define helper functions for different search criteria
def get_search_results(selected_option, search_query):
    if selected_option == "Category":
        return searchByCategory(search_query)
    elif selected_option == "Location":
        return searchByLocation(search_query)
    elif selected_option == "Title":
        return searchByTitle(search_query)
    else:
        return {}

