from json import load
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os

class TwilioHelper():
    def __init__(self):
        with open("credentials.json") as f:
            creds = load(f)
        self.account_sid = creds["twilio"]["account_sid"]
        self.auth_token = creds["twilio"]["auth_token"]
        self.client = Client(self.account_sid, self.auth_token)
        self.twilio_number = creds["twilio"]["number"]

    def message_response(self, incoming_msg) -> (str, str):
        resp = MessagingResponse()
        incoming_msg.toLower()
        if(incoming_msg == "Hello"):
            resp.message("Welcome! What service are you looking for? \nPlease reply with ONE of the following: \n1. Shelter\n2. Food\n3. Personal Hygiene")
        elif(incoming_msg == "Bye"):
            resp.message("Good luck!")
        else:
            if(incoming_msg == "Shelter"):
                resp.message("Please follow this link to confirm location-based services: \n")
            elif(incoming_msg == "Food"):
                resp.message("Please follow this link to confirm location-based services: \n")
            elif(incoming_msg == "Personal Hygiene"):
                resp.message("Please follow this link to confirm location-based services: \n")
            user_number = get_user_number()
            return (user_number, incoming_msg)
        return ("", "")

    def get_user_number(self):
        return str(client.messages.list(to = self.twilio_number)[0].from_)

    def text_user(self, message: str, user_number: str) -> None:
        message = self.client.messages.create(body = message, to = user_number, from_ = self.twilio_number)
