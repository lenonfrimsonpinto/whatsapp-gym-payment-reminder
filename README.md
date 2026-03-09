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





Step 1: Create Google Sheets Database

Create a Google Sheet named:

GymMembers

Inside this file create two sheets:

GymMembers

PaymentHistory

Sheet 1: GymMembers

Column description:

Member ID → Unique identifier for each member

Name → Member name

Phone → Phone number with country code

Join Date → Date the member joined

Payment Due Date → Next payment due date

Amount → Monthly membership fee

Payment Status → Pending or Paid

Payment Date → Date when payment was received

Mode of Payment → UPI, Cash, Card, etc.


Sheet 2: PaymentHistory

Create another sheet named:

PaymentHistory - This sheet stores all historical payment records.

Step 2: Enable Google Sheets API

Go to Google Cloud Console
https://console.cloud.google.com/

Create a new project

Navigate to:

APIs & Services → Library

Search and enable:

Google Sheets API

Step 3: Create Service Account

Go to:

APIs & Services → Credentials

Click:

Create Credentials → Service Account

Create the service account

Generate a JSON key

Download the file.

Example:

credentials.json

Step 4: Share Google Sheet Access

Open your GymMembers Google Sheet.

Click Share.

Add the service account email found in your credentials file.

Example:

gym-bot@project-id.iam.gserviceaccount.com

Give Editor access.

Step 5: Install Dependencies

Install the required Python packages.

pip install -r requirements.txt

Contents of requirements.txt:

gspread
pandas
pywhatkit
pyautogui
Pillow
python-dateutil
pywin32
google-auth

step 6: Place Required Files

Place the following files inside the project folder:

credentials.json
payment_qr.png
gym_automation.py

Step 7: Update Script Configuration

Open gym_automation.py and ensure the credentials file path is correct.

gc = gspread.service_account(filename="credentials.json")

Step 8: Login to WhatsApp Web

Before running the script, login to WhatsApp Web.

Open:

https://web.whatsapp.com

Scan the QR code using your phone.

The automation will use this session.

Step 9: Run the Script

Execute the program using:

python gym_automation.py

System Workflow

Python reads member data from Google Sheets.

If a member's payment due date is today or earlier, a WhatsApp reminder is sent.

A QR code image is automatically attached for payment.

When Payment Status becomes Paid, the system:

Stores payment details in the PaymentHistory sheet

Updates the next payment due date by one month

Resets payment status and payment fields

Security Note

Never upload your credentials file to GitHub.
credentials.json



Automating the Script with Task Scheduler (Windows)

To make the system fully automated, you can schedule the Python script to run automatically using Windows Task Scheduler. This allows reminders to be sent daily without manually running the program.

Step 1: Open Task Scheduler

Press Windows Key

Search for Task Scheduler

Open the application

Step 2: Create a New Task

Click Create Basic Task

Enter a name

Example:

Gym Payment Automation

Click Next.

Step 3: Choose Trigger

Select how often the script should run.

Recommended option:

Daily

Set the preferred time (for example 9:00 AM) when reminders should be sent.

Click Next.

Step 4: Choose Action

Select:

Start a Program

Click Next.

Step 5: Configure Program Path

In Program/script, select the Python executable.

Example:

C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\python.exe
Step 6: Add Script Path

In Add arguments, enter the path to the automation script.

Example:

"C:\Users\YourUsername\Documents\gym-payment-automation\gym_automation.py"
Step 7: Set Start Folder

In Start in, enter the folder containing the script.

Example:

C:\Users\YourUsername\Documents\gym-payment-automation
Step 8: Save the Task

Click Finish.

Your automation will now run automatically at the scheduled time.

esting the Task

To verify that the task works correctly:

Open Task Scheduler

Locate the created task

Right-click the task

Click Run

If configured correctly, the Python script will start and the automation will execute.

Important Notes

For the automation to work properly:

The laptop must be powered on

The system should not be in sleep mode

Internet connection must be active

WhatsApp Web must remain logged in





