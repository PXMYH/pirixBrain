import os
import yagmail

def send_sms(message: str):
    username = os.environ.get("TEXTNOW_USERNAME")
    destination_phone_number = os.environ.get("DESTINATION_PHONE_NUMBER")

    print(f"sending sms {message}")

def send_email(message: str):
    username = os.environ.get("GMAIL_USERNAME")
    password = os.environ.get("GMAIL_APP_PASSWORD")
    destination = os.environ.get("DESTINATION_EMAIL")
    yag = yagmail.SMTP(username, password)
    contents = [message]
    
    yag.send(destination, 'billing notification', contents)
