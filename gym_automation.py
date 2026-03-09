import gspread
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pywhatkit
import pyautogui
import time
from PIL import Image
import io
import win32clipboard

# ===== CONFIG =====
QR_IMAGE_PATH = r"payment_qr.png"

# ===== FUNCTION TO COPY IMAGE =====
def copy_image_to_clipboard(image_path):
    image = Image.open(image_path)
    output = io.BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


# ===== CONNECT TO GOOGLE SHEET =====
gc = gspread.service_account(filename="credentials.json")

members_sheet = gc.open("GymMembers").worksheet("GymMembers")
history_sheet = gc.open("GymMembers").worksheet("PaymentHistory")


data = members_sheet.get_all_records()
df = pd.DataFrame(data)

today = datetime.today().date()


for i, row in df.iterrows():
    memberid=row['Member ID']
    name = row['Name']
    phone = "+{}".format(row['Phone'])
    status = str(row['Payment Status']).lower()
    amount = row['Amount']
    due_date = datetime.strptime(row['Payment Due Date'], "%Y-%m-%d").date()

    # ================= SEND REMINDER =================
    if due_date <= today and status == "pending":

        message = f"""Hello {name}, this is a reminder that your gym membership payment of ₹{amount} is due on {due_date}.
Please make the payment using the QR code below and share the screenshot after payment.
Thank you! 💪
"""

        print("Sending reminder to", name)

        pywhatkit.sendwhatmsg_instantly(phone, message, wait_time=15, tab_close=False)

        time.sleep(5)

        # Copy QR Image
        copy_image_to_clipboard(QR_IMAGE_PATH)

        time.sleep(2)

        pyautogui.hotkey("ctrl", "v")
        time.sleep(2)

        pyautogui.press("enter")

        time.sleep(5)

        pyautogui.hotkey("ctrl", "w")

        time.sleep(10)


    # ================= STORE PAYMENT HISTORY =================
    if status == "paid":

        payment_date = row['Payment Date']
        mode = row['Mode of Payment']

        history_sheet.append_row([
            memberid,
            name,
            row['Phone'],
            payment_date,
            amount,
            mode
        ])

        print(f"Payment history stored for {name}")


        # ================= UPDATE NEXT DUE DATE =================
        next_due = datetime.strptime(row['Payment Due Date'], "%Y-%m-%d") + relativedelta(months=1)

        members_sheet.update_cell(i+2, 5, next_due.strftime("%Y-%m-%d"))
        members_sheet.update_cell(i+2, 7, "Pending")
        members_sheet.update_cell(i+2,8,"")
        members_sheet.update_cell(i+2,9,"")

        print(f"Updated {name} → Next Due: {next_due.date()}")