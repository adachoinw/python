from twilio.rest import Client

account_sid = "<twilio account sid>"
auth_token = "<twilio auth token>"
TWILIO_VIRTUAL_NUMBER = "+<twilio number>"
TWILIO_VERIFIED_NUMBER = "+<my number>"


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        # Prints if successfully sent.
        print(message.sid)
