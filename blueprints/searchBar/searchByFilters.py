from flask import Blueprint, request, jsonify, make_response, current_app
from bson.json_util import dumps
from Database.advertisementSearch import search_ads_by_date, search_ads_by_location, search_ads_by_title, search_ads_by_category
from datetime import datetime, timedelta


searchByFilters_bp = Blueprint("searchByFilters", __name__)

@searchByFilters_bp.route('/filter-ads', methods=['GET'])
def search_recent_ads():
    selected_option = request.args.get('selectedOption')
    search_query = request.args.get('searchQuery')
    start_Date = convert_date_format(request.args.get('startDate'))
    end_date = convert_date_format(request.args.get('endDate'))
    category = request.args.get('category')
    print(selected_option,search_query,start_Date, end_date,category)
    if not selected_option :
        return jsonify({"error": "Missing search criteria"}), 400

    if selected_option == "Date":
        # Implement your logic to search by date
        data = search_ads_by_date(start_Date, end_date)
    elif selected_option == "Category":
        # Implement your logic to search by category
        if category == "Land Sale":
            data = search_ads_by_category("LandSale_Advertisement")
        elif category == "House Sale":
            data = search_ads_by_category("HouseSale_Advertisement")
        elif category == "Marriage Proposals":
            data = search_ads_by_category("Marriage_Proposal")
    elif selected_option == "Location":
        # Implement your logic to search by location
        data =search_ads_by_location(search_query)

    elif selected_option == "Title":
        # Implement your logic to search by title
        data =search_ads_by_title(search_query)
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




def convert_date_format(original_date_str):
    try:
        # Parse the original date
        original_date = datetime.strptime(original_date_str, "%Y-%m-%d")

        # Subtract one day to get "2023-07-31"
        new_date = original_date - timedelta(days=1)

        # Add the time "18:30:00.000"
        new_date_with_time = new_date.replace(hour=18, minute=30, second=0, microsecond=0)

        # Format the resulting date with timezone offset
        formatted_date = new_date_with_time.strftime("%Y-%m-%dT%H:%M:%S.%f+00:00")

        return formatted_date
    except ValueError:
        return None