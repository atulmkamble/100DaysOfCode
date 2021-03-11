from twilio.rest import Client

# TODO: Add your Twilio details
TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''
TWILIO_VIRTUAL_NUMBER = ''
TWILIO_VERIFIED_NUMBER = ''


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
