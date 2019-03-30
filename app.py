import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/",methods=["GET"])
def main():
    return render_template("index.html")

@app.route("/organizations",methods=["GET"])
def organizations():
    return render_template("organization.html")

if __name__ == '__main__':
    app.run()
