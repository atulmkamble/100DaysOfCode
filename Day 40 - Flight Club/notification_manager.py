from twilio.rest import Client
import smtplib

# TODO: Add your twilio account details and your email id and password
TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_VIRTUAL_NUMBER = ''
TWILIO_VERIFIED_NUMBER = ''
MAIL_PROVIDER_SMTP_ADDRESS = 'smtp.gmail.com'
MY_EMAIL = ''
MY_PASSWORD = ''


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, msg):
        message = self.client.messages.create(
            body=msg,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)

    def send_emails(self, emails, msg, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{msg}\n{google_flight_link}".encode('utf-8')
                )
