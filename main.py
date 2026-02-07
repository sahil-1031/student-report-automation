import pandas as pd
import os
import smtplib
from email.message import EmailMessage
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Read student data
data = pd.read_csv("students.csv")
data.columns = data.columns.str.strip()

#Make reports folder in which pdfs will be saved
os.makedirs("reports", exist_ok=True)

def calculate_grade(percentage):
    if percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

def generate_pdf(name, total, percentage, grade, result, file_path):
    pdf = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    # Title
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(width / 2, height - 1 * inch, "STUDENT REPORT CARD")

    # Divider
    pdf.line(50, height - 1.2 * inch, width - 50, height - 1.2 * inch)

    # Content
    pdf.setFont("Helvetica", 12)
    y = height - 2 * inch

    pdf.drawString(80, y, f"Student Name : {name}")
    y -= 30
    pdf.drawString(80, y, f"Total Marks : {total}")
    y -= 30
    pdf.drawString(80, y, f"Percentage : {percentage:.2f}%")
    y -= 30
    pdf.drawString(80, y, f"Grade       : {grade}")
    y -= 30
    pdf.drawString(80, y, f"Result      : {result}")

    # Footer
    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawCentredString(width / 2, 50, "This is a system-generated report.")

    pdf.save()

def send_email(receiver_email, student_name, pdf_path):
    msg = EmailMessage()
    msg["Subject"] = "Student Report Card"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receiver_email

    msg.set_content(
        f"""
Dear {student_name},

Please find attached the report card.

Regards,
School Administration
"""
    )

    with open(pdf_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(pdf_path)
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

# MAIN AUTOMATION LOOP
for index, row in data.iterrows():
    total = row["MATHS"] + row["SCIENCE"] + row["ENGLISH"]
    percentage = total / 3
    grade = calculate_grade(percentage)
    result = "Pass" if percentage >= 40 else "Fail"

    pdf_path = f"reports/{row['NAME']}_report.pdf"

    generate_pdf(
        row["NAME"],
        total,
        percentage,
        grade,
        result,
        pdf_path
    )

    send_email(row["EMAIL"], row["NAME"], pdf_path)

    print(f"Report generated & emailed to {row['NAME']}")

print("🎉 Automation completed successfully!")
