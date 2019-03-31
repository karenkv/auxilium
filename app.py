import json
from flask import Flask, render_template, request
from twilio_helper import TwilioHelper
import session_manager
from google_maps_helper import GoogleMapsHelper
from json_form_handler import JSONFormHandler
import urllib.parse

app = Flask(__name__)
twilio_object = TwilioHelper()
google_maps_object = GoogleMapsHelper()
json_form_object = JSONFormHandler()

@app.route("/",methods=["GET"])
def main():
    return render_template("index.html")

@app.route("/organizations",methods=["GET"])
def organizations():
    return render_template("organizations.html")

@app.route("/sms", methods=["POST"])
def sms():
    body = request.values.get('Body', None)
    twilio_object.message_response(body)

@app.route("/sms/<user_number>/<desire>", methods=["GET"])
def link(user_number, desire):
    session = session_manager.getSession(user_number)
    if session is None:
        return "Error: Session has expired."
    else:
        searchFor = json_form_object.findByType(desire)
        closestOrgs = google_maps_object.get_min(searchFor)
        response = "The closest organizations for x around you are:"
        for org in closestOrgs:
            mapsLink = googleLinkCreator(org[0])
            response += "\n" + org[0] + "\n" + "Google Maps Direction: " + mapsLink + "\n" + org[1] + " mi away."
        twilio_object.text_user(response, user_number)

def googleLinkCreator(orgName):
    return "https://www.google.com/maps/search/?api=1&" + urllib.parse.urlencode([('query',orgName)]) + "+in+los+angeles+ca"


if __name__ == '__main__':
    app.run()
