from json import load
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

class TwilioHelper():
    def __init__(self):
        with open("credentials.json") as f:
            creds = load(f)
        self.account_sid = creds["twilio"]["account_sid"]
        self.auth_token = creds["twilio"]["auth_token"]
        self.client = Client(self.account_sid, self.auth_token)
        self.twilio_number = creds["twilio"]["number"]

    def message_response(self, incoming_msg) -> str:
        resp = MessagingResponse()
        if(incoming_msg == "Hello"):
            resp.message("Welcome!")
        elif(incoming_msg == "Bye"):
            resp.message("Good luck!")
        return str(resp)

    def text_user(self, message: str, user_number: str) -> None:
        message = self.client.messages.create(body = message, to = user_number, from_ = self.twilio_number)
