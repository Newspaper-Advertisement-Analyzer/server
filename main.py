from flask import Flask

#import blue prints
from blueprints.advertisementMap.adverisementMap import advertisementsMap_bp
from blueprints.authentication.signup import signUp_bp
from blueprints.authentication.signin import signIn_bp
from blueprints.uploads.upload import upload_bp




from datetime import datetime, timedelta
import random

from sendEmail.sendVerificstionCode import send_advanced_email

verification_codes = {}


app = Flask(__name__)
app.register_blueprint(advertisementsMap_bp)
app.register_blueprint(signUp_bp)
app.register_blueprint(signIn_bp)
app.register_blueprint(upload_bp)



app.config['UPLOAD_FOLDER_IMG'] = 'uploadsimg'
app.config['UPLOAD_FOLDER_PDF'] = 'uploadspdf'


if __name__ == '__main__':
    app.run(debug=True)
