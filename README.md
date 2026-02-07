👨‍💻 Author: Sahil Patel
# 🎓 Automated Student Report Generator (Python Automation)

A real-world Python automation project that reads student marks from a CSV file, generates professional PDF report cards, and emails them automatically using Gmail SMTP.

---

## 🚀 Features

- 📊 Reads student data from CSV
- 🧮 Calculates total & percentage automatically
- 🏆 Assigns grade (A / B / C / Fail)
- 📄 Generates professional PDF report cards
- 📧 Sends report via email automatically
- 🔐 Uses environment variables for security
- ⚡ Fully automated — no manual work required

---

## 🛠️ Tech Stack

- Python
- Pandas
- ReportLab (PDF generation)
- SMTP (Email automation)
- Python-dotenv

---

## 📁 Project Structure

student_report_automation/
│
├── main.py
├── students.csv                          # SAMPLE DATASET
├── requirements.txt
└── reports/ (auto-generated)


---
## ⚙️ How to Run the Project

1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/student-report-automation.git
cd student-report-automation

2️⃣ Create virtual environment
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Create .env file

Create a file named .env and add:

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_16_digit_app_password

5️⃣ Run the automation
python main.py


📧 Email Automation Note

Gmail requires an App Password for SMTP login.

Steps:

Enable 2-Step Verification in Google Account

Generate App Password

Use it in .env

🎯 Real World Use Case

This project automates the manual work done by schools/coaching institutes:

Generating report cards

Sending them to students/parents

Reducing human effort and errors



