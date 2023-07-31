from Flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import timesheet
import validation

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_time_entry", methods=['POST'])
def add_time_entry():
    try:
        date = request.form["date"]
        date = date.validate_date(date)

        start_time = request.form["start_time"]
        start_time

    except ValueError as e:
        return