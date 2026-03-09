# whatsapp-gym-payment-reminder
Automated Gym Payment Reminder System that tracks member dues using Google Sheets and Python. The system sends WhatsApp reminders with a QR code for payment, records payment history, updates next due dates, and manages membership payment status automatically to simplify gym fee tracking and reduce manual work.

Features

Track gym members using Google Sheets

Send WhatsApp reminders automatically for due payments

Attach QR code image for easy payment

Store payment history automatically

Update next due date after payment

Reset payment status for the next cycle

Fully automated workflow using Python

Technologies Used

Python

Google Sheets API

gspread

pandas

pywhatkit

pyautogui

Pillow

python-dateutil

pywin32


gym-payment-automation
│
├── gym_automation.py
├── payment_qr.png
├── requirements.txt
├── README.md
└── .gitignore



Step 1: Create Google Sheets Database

Create a Google Sheet named:

GymMembers

Inside this file create two sheets:

GymMembers

PaymentHistory
