from json import load
from twilio.rest import Client

class TwilioHelper():
    def __init__(self):
        with open("credentials.json") as f:
        creds = load(f)
        self.account_sid = creds["twilio"]["account_sid"]
        self.auth_token = creds["twilio"]["auth_token"]
        self.client = Client(self.account_sid, self.auth_token)
