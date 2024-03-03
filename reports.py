#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file_path, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(file_path)
    report_title = Paragraph(title, styles["h1"])
    report_body = Paragraph(paragraph, styles["BodyText"])
    report.build([report_title, report_body])
