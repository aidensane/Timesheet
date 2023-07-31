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
        date = validation.validate_date(date)

        start_time = request.form["start_time"]
        start_time = validation.validate_time(start_time)

        end_time = request.form["end_time"]
        end_time = validation.validate_time(end_time)

        task = request.form["task"]
        task = validation.validate_task(task)

        timesheet.add_time_entry_date(date, start_time.strftime("%H:%H"), end_time.strftime("%H:%H"), task)
        


    except ValueError as e:
        return