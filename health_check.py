#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

def check_cpu_usage():
    # Check CPU usage
    print("check_cpu_usage")
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage > 80

def check_disk_space():
    # Check available disk space
    print("check_disk_space")
    disk_usage = shutil.disk_usage("/")
    free_space_percentage = disk_usage.free / disk_usage.total * 100
    return free_space_percentage < 20

def check_memory():
    # Check available memory
    print("check_memory")
    available_memory = psutil.virtual_memory().available / (1024 * 1024)  # in MB
    return available_memory < 500

def check_localhost():
    # Check if hostname "localhost" resolves to "127.0.0.1"
    print("check_localhost")
    return socket.gethostbyname("localhost") != "127.0.0.1"

def main():
    sender = "automation@example.com"
    recipient = "student-04-73fa1d015d00@example.com"
    subject_prefix = "Error - "

    issues = []
    if check_cpu_usage():
        issues.append("CPU usage is over 80%")
    if check_disk_space():
        issues.append("Available disk space is less than 20%")
    if check_memory():
        issues.append("Available memory is less than 500MB")
    if check_localhost():
        issues.append("localhost cannot be resolved to 127.0.0.1")

    # Send email if issues are detected
    if issues:
        subject = f"{subject_prefix}Health Check Report"
        body = "Please check your system and resolve the following issues:\n\n"
        body += "\n".join(issues)
        body += "\n\nPlease check your system and resolve the issue as soon as possible."

        email_message = emails.generate_email(sender, recipient, subject, body)
        emails.send_email(email_message)

if __name__ == "__main__":
    main()
