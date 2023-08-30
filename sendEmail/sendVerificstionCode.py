import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
from dotenv import load_dotenv

load_dotenv('..env')

FROM_EMAIL: str = os.getenv('EMAIL')
PASSWORD: str = os.getenv('EMAILPASSWORD')
# EMAIL="kodeblitz@outlook.com"
# EMAILPASSWORD="9HX)T2Y%[waYx~9#~{388${n]jk@gc%v"


def send_advanced_email(user_email, verification_code):
    HOST = "smtp-mail.outlook.com"
    PORT = 587
    # FROM_EMAIL = "kodeblitz@outlook.com"  # Update with your email
    # PASSWORD = "9HX)T2Y%[waYx~9#~{388${n]jk@gc%v"  # Update with your password

    msg = MIMEMultipart()
    
    msg["From"] = FROM_EMAIL
    msg["To"] = user_email
    msg["Subject"] = "Account Verification"
    
    # Create HTML body
    html_body = f"""
    <html>
    <head></head>
    <body>
        <h2>Welcome to Your App!</h2>
        <p>Dear user,</p>
        <p>Thank you for registering with us. To complete your registration, please use the verification code below:</p>
        <p><strong>{verification_code}</strong></p>
        <p>This code is valid for 1 minute.</p>
        <p>Click <a href="https://www.ApeWebsiteEka.com/verify">here</a> to verify your account. Meka thama hadala na yako</p>
        <p>If you did not sign up for an account, you can safely ignore this email.</p>
        <br>
        <p>Best regards,</p>
        <p>Ads Analyzer</p>
        <hr>
        <img src="https://images-platform.99static.com//GrTXS_qDmn1kmkhoxGcQH_cQdWU=/598x0:1386x788/fit-in/500x500/99designs-contests-attachments/47/47677/attachment_47677934" alt="Your App Logo">
    </body>
    </html>
    """
    
    # Attach the HTML body
    msg.attach(MIMEText(html_body, "html"))

    try:
        smtp = smtplib.SMTP(HOST, PORT)
        smtp.starttls()
        smtp.login(FROM_EMAIL, PASSWORD)
        smtp.sendmail(FROM_EMAIL, user_email, msg.as_string())
        smtp.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

send_advanced_email("lisives254@trazeco.com",123)