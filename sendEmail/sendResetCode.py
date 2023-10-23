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
subject = "Forgot Password Recovery"


def send_reset_code(userEmail, ResetCode):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = userEmail
    msg['Subject'] = subject

    html_body = f"""
    <html>
    <head></head>
    <body>
        <h2>Password Reset</h2>
        <p>Dear user,</p>
        <p>We received a request to reset your password. If you did not make this request, you can ignore this email.</p>
        <p>To reset your password, please use the code below:</p>
        <p><strong>{ResetCode}</strong></p>
        <p>This link is valid for 1 minute.</p>
        <p>If you have any issues, please contact our support team.</p>
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
            print("Password reset email sent!")
    except:
        print("Error: Email not sent!")

# Usage example:
# reset_link = "https://www.example.com/reset_password?token=your_reset_token"
# send_email("user@example.com", reset_link)
