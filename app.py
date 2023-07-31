from Flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import timesheet
import validate

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_time_entry", methods=['POST'])
def add_time_entry():
    try:
        date = request.form["date"]
        date = validate.validate_date(date)

        start_time = request.form["start_time"]
        start_time = validate.validate_time(start_time)

        end_time = request.form["end_time"]
        end_time = validate.validate_time(end_time)

        task = request.form["task"]
        task = validate.validate_task(task)

        timesheet.add_time_entry_date(date, start_time.strftime("%H:%H"), end_time.strftime("%H:%H"), task)
        return redirect(url_for("index", message="Time entry added successfully!"))

    except ValueError as e:
        return render_template("index.html", error=str(e))
    
@app.route("/timesheet")
def view_timesheet():
    timesheet_data = timesheet.get_timesheet_data()
    return render_template("timesheet.html", timesheet_data= timesheet_data)

if __name__ == "__main__":
    app.run(debug=True)