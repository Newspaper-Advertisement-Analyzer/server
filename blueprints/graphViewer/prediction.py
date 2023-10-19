from flask import Blueprint, request, jsonify, make_response, current_app
from pricePrediction.houseSalePrediction import combined_df

forecastedPrices_bp = Blueprint("forecastedPrices", __name__)


@forecastedPrices_bp.route('/forecasted_prices', methods=['GET'])
def get_forecasted_prices():
    # Add your data processing and plotting logic here
    #
    # Assuming `combined_df` contains the forecasted prices DataFrame
    forecasted_data = combined_df.to_dict(orient='list')
    return jsonify(forecasted_data)
