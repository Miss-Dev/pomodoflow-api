import smtplib
from email.mime.text import MIMEText
import os

def send_email(subject: str, body: str):
    user = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    to = os.getenv("EMAIL_TO")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = to

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(user, password)
        server.send_message(msg)