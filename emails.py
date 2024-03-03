#!/usr/bin/env python3

from email.message import EmailMessage
import smtplib
import os

def generate_email(sender, recipient, subject, body, attachment_path=None):
    message = EmailMessage()
    message.set_content(body)

    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    if attachment_path:
        with open(attachment_path, "rb") as file:
            message.add_attachment(file.read(), maintype="application", subtype="pdf", filename=os.path.basename(attachment_path))

    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    
    mail_server.send_message(message)
    print("email sent")
    
    mail_server.quit()