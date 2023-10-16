from flask import Blueprint, request, jsonify, make_response, current_app
from Database.feedback import saveFeedback

feedback_bp = Blueprint("feedback", __name__)


@feedback_bp.route('/submitFeedback', methods=['POST'])
def submitFeedback():
    try:
        data = request.get_json()
        # Save the feedback data in the database
        result = saveFeedback(data.get("rating"), data.get("feedback"),
                              data.get("publish"), data.get("userID"))

        # Return a success message as a response.
        if result.inserted_id:
            # Return a success message if the feedback was successfully saved
            return {"message": "Feedback saved successfully"}
        else:
            # Return an error message if there was an issue saving the feedback
            return {"error": "Failed to save feedback"}
    except Exception as e:
        # Return an error message if there was an issue processing or saving the feedback data.
        return jsonify({"error": str(e)})
