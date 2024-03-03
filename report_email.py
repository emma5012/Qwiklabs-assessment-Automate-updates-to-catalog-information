#!/usr/bin/env python3

import os
import datetime
import reports
import emails

def process_data(directory):
    data = ""
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                name = lines[0].strip()
                weight = lines[1].strip()
                data += f"name: {name}<br/>weight: {weight}<br/><br/>"

    return data

def main():
    directory = "supplier-data/descriptions"
    title = f"Processed Update on {datetime.date.today()}"
    data_paragraph = process_data(directory)
    attachment = "/tmp/processed.pdf"

    reports.generate_report(attachment, title, data_paragraph)
    
    sender = "automation@example.com"
    recipient = "student-04-73fa1d015d00@example.com" 
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    email_message = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(email_message)

if __name__ == "__main__":
    main()

