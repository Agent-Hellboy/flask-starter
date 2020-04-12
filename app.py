from flask import Flask, render_template, request, redirect, jsonify, url_for, flash


import random
import string
import logging
import json
import httplib2
import requests


app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/Implinks")
def showMain():
    a = "https://flask.palletsprojects.com/en/1.1.x/quickstart/"
    b = "https://github.com/pallets/flask"
    c = "https://medium.com/bhavaniravi/build-your-1st-python-web-app-with-flask-b039d11f101c"
    links = [a, b, c]
    return render_template("Implinks.html", links=links)


if __name__ == "__main__":
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
