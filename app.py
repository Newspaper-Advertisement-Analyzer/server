from flask import Flask
from flask_cors import CORS

# Import your blueprints here
from blueprints.advertisementMap.adverisementMap import recentAdLocation_bp
from blueprints.authentication.signup import signUp_bp
from blueprints.authentication.signin import signIn_bp
from blueprints.uploads.upload import upload_bp
from blueprints.graphViewer.averagePrice import averageSale_bp
from blueprints.graphViewer.ad_distribution import adDistribution_bp
from blueprints.graphViewer.marriagePoposalCatergory import categorizebyAge_bp
from blueprints.graphViewer.houseSalebyCity import houseSalebyCity_bp
from blueprints.searchTable.recentAdvertisement import recentAd_bp
from blueprints.advertisementCards.popularAdvetisements import popularAd_bp
from blueprints.searchBar.searchByFilters import searchByFilters_bp
from blueprints.reports.reportSave import reports_bp
from blueprints.reports.getReports import getreports_bp
from blueprints.counts.counts import counts_bp
from blueprints.manageUser.viewUsers import getAllUsers_bp
from blueprints.manageUser.deleteUser import deleteUser_bp
from blueprints.feedback.submitFeedback import feedback_bp
# Import other necessary modules
from datetime import datetime, timedelta
import random
from sendEmail.sendVerificstionCode import send_advanced_email

# Create the Flask app
app = Flask(__name__)

# Enable CORS for the app
CORS(app)

# Register your blueprints
app.register_blueprint(recentAdLocation_bp)
app.register_blueprint(signUp_bp)
app.register_blueprint(signIn_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(averageSale_bp)
app.register_blueprint(adDistribution_bp)
app.register_blueprint(categorizebyAge_bp)
app.register_blueprint(houseSalebyCity_bp)
app.register_blueprint(recentAd_bp)
app.register_blueprint(popularAd_bp)
app.register_blueprint(searchByFilters_bp)
app.register_blueprint(reports_bp)
app.register_blueprint(getreports_bp)
app.register_blueprint(counts_bp)
app.register_blueprint(getAllUsers_bp)
app.register_blueprint(deleteUser_bp)
app.register_blueprint(feedback_bp)

# Configure any app-specific settings here
app.config['UPLOAD_FOLDER_IMG'] = 'uploadsimg'
app.config['UPLOAD_FOLDER_PDF'] = 'uploadspdf'

# Optionally, you can add more configuration settings or initialize other components here.

# Define your routes and other application logic as needed.

if __name__ == '__main__':
    # This block will only execute if you run this script directly (not when imported)
    app.run(debug=True)
