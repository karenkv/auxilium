from json import load
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os
import json_form_handler
import session_manager

#CREATE EXTRA STATE FOR WAITING FOR LOCATION RESPONSE

def buildLocationLink(pNumber, desire):
    d = "shelter"
    if desire is 2:
        d = "food"
    elif desire is 3:
        d = "hygiene"
    return " https://3fc8be3e.ngrok.io/sms/" + pNumber + "/" + d;

def state0Response():
    return "Welcome to Auxilium! What service are you looking for? \n\nPlease reply with ONE of the following numbers: \n1. Shelter\n2. Food\n3. Hygiene"

def state1Response(pNumber, userResponse):
    response = "Please click the following link to confirm location-based services:\n"
    if userResponse is "1" or userResponse.lower() is "shelter":
        response += buildLocationLink(pNumber, 1)
    elif userResponse is "2" or userResponse.lower() is "food":
        response += buildLocationLink(pNumber, 2)
    elif userResponse is "3" or userResponse.lower() is "hygiene":
        response += buildLocationLink(pNumber, 3)
    else:
        return "Error, please send 1 for shelter, 2 for food, or 3 for hygiene."
    response += "\n\nPlease wait after clicking link. Do not send messages while Auxilium is calculating organizations near you. \n\nSend BYE to end the session."
    return response

def state2Response(pNumber, userResponse):
    if userResponse.upper() is "STOP":
        session_manager.deleteSession(pNumber)
        return "Thank you for using Auxilium's services! We are now ending this session. Please message again to start a new session."
    else:
        return "Sorry, due to data constraints we can only send out 1 link at a time. Please wait while Auxilium is calculating organizations near you."

def state3Response(pNumber, userResponse):
    if userResponse is "1":
        session_manager.setState(pNumber, 1)
        return state0Response()
    elif userResponse is "2":
        session_manager.deleteSession(pNumber)
        return "Thank you for using Auxilium's services! We are now ending this session. Please message again to start a new session."
    return "Error, please send 1 to continue services or 2 to end the session."

class TwilioHelper():
    def __init__(self):
        '''
        Initializes TwilioHelper class with account_sid, auth_token, client, and phone number with credentials json file.
        '''
        with open("credentials.json") as f:
            creds = load(f)
        self.account_sid = creds["twilio"]["account_sid"]
        self.auth_token = creds["twilio"]["auth_token"]
        self.client = Client(self.account_sid, self.auth_token)
        self.twilio_number = creds["twilio"]["number"]

    def message_response(self, incoming_msg) -> str:
        '''
        Handles messaging response from client. Takes an incoming message and returns tuple with user's number and service requested,
        unless incoming message is hello/bye/invalid.
        '''

        user_number = self.get_user_number()
        session = session_manager.getSession(user_number)
        if session is None:
            session_manager.createSession(user_number)
            session = session_manager.getSession(user_number)

        state = session["state"]

        resp = MessagingResponse()
        if state is 0:
            resp.message(state0Response())
            session_manager.setState(user_number, 1)
        elif state is 1:
            resp.message(state1Response(user_number, incoming_msg))
        elif state is 2:
            resp.message(state2Response(user_number, incoming_msg))
        elif state is 3:
            resp.message(state3Response(user_number, incoming_msg))
        else:
            resp.message("Error: Session is now closing.")
            session_manager.deleteSession(user_number)
        return str(resp)

    def get_user_number(self) -> str:
        '''
        Gets user number from client messages list.
        '''
        return str(self.client.messages.list(to = self.twilio_number)[0].from_)

    def text_user(self, message: str, user_number: str) -> str:
        '''
        Takes a message and phone number and texts the user's number the specified message.
        '''
        message = self.client.messages.create(body = message, to = user_number, from_ = self.twilio_number)
        return str(message)
