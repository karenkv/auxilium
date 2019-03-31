import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")

@app.route("/organizations", methods=["GET"])
def organizations():
    return render_template("organizations.html")

@app.route("/add-new-org", methods=["POST"])
def add_new_org():
    req_data = request.form

    # print(req_data)

    # with open('org_database.json') as f:
    #     data = json.load(f)
    
    # data.update(req_data)

    # with open('org_database.json', 'w') as f:
    #     json.dump(data, f)

    return 'done'

if __name__ == '__main__':
    app.run()
