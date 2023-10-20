import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


import os
from dotenv import load_dotenv

load_dotenv('./.env')

FROM_EMAIL: str = os.getenv('GMAIL')
PASSWORD: str = os.getenv('GMAILPASSWORD')

# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = FROM_EMAIL
smtp_password = PASSWORD

sender = 'Newspaper-Advertisement-Analyzer'
subject = "Account Verification"


def send_email(userEmail, verficationCode):

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = userEmail
    msg['Subject'] = subject

    html_body = f"""
    <html>
    <head></head>
    <body>
        <h2>Welcome to Our App!</h2>
        <p>Dear user,</p>
        <p>Thank you for registering with us. To complete your registration, please use the verification code below:</p>
        <p><strong>{verficationCode}</strong></p>
        <p>This code is valid for 1 minute.</p>
        <p>Click <a href="https://www.ApeWebsiteEka.com/verify">here</a> to verify your account. This is not implemented yet</p>
        <p>If you did not sign up for an account, you can safely ignore this email.</p>
        <br>
        <p>Best regards,</p>
        <p>Ads Analyzer</p>
        <hr>
        <img src="https://firebasestorage.googleapis.com/v0/b/learning-3419a.appspot.com/o/Logo%2Flogowithbrand.png?alt=media&token=e4b3f874-3616-417e-9291-4bfcc18e0438" 
        alt="Your App Logo" 
        width="250px"
        height="auto">
    </body>
    </html>
    """

    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender, userEmail, msg.as_string())
            print("Email sent!")
    except:
        print("Error: Email not sent!")

# send_email("wiwesi7288@ustorp.com", 123456)