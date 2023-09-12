from flask import Flask

#import blue prints
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

from datetime import datetime, timedelta
import random

from sendEmail.sendVerificstionCode import send_advanced_email

verification_codes = {}


app = Flask(__name__)
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

app.config['UPLOAD_FOLDER_IMG'] = 'uploadsimg'
app.config['UPLOAD_FOLDER_PDF'] = 'uploadspdf'


if __name__ == '__main__':
    app.run(debug=True)
