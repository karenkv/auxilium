import json
from flask import Flask, render_template, request
import twilio_helper
import session_manager
import google_maps_helper
import json_form_handler
import urllib.parse

app = Flask(__name__)
twilio_object = TwilioHelper()
google_maps_object = GoogleMapsHelper()
json_form_object = JSONFormHandler()

@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")

@app.route("/organizations", methods=["GET"])
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
            response += "\n" + org[0] + "\n" + "Google Maps: " + mapsLink + "\n" + org[1] + " mi away."
        response += "Please send 1 to continue services or 2 to end the session."
        twilio_object.text_user(response, user_number)
        session_manager.setState(user_number, 3)

def googleLinkCreator(orgName):
    return "https://www.google.com/maps/search/?api=1&" + urllib.parse.urlencode([('query',orgName)]) + "+in+los+angeles+ca"

@app.route("/add-new-org", methods=["POST"])
def add_new_org():
    req_data = request.form

    print(req_data)

    # with open('org_database.json') as f:
    #     data = json.load(f)

    # data.update(req_data)

    # with open('org_database.json', 'w') as f:
    #     json.dump(data, f)

    return 'done'

if __name__ == '__main__':
    app.run()
