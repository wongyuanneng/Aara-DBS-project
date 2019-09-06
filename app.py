from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import requests

#configure app
app = Flask(__name__)

#configure sessions
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

goals = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods = ["POST"])
def submitForm():
    for item in request.form:
        newGoal = request.form.get(item)
        goals.append(newGoal)
        goalAnalysis(newGoal)
    return redirect("/")

def goalAnalysis(newGoal):
    print(newGoal)
