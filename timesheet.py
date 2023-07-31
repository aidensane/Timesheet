import csv
from datetime import datetime

TIMESHEET_FILE = "timesheet.csv"

def create_timesheet_file():
    with open(TIMESHEET_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Start Time", "End Time", "Task"])

def add_time_entry(date, start_time, end_time, task):
    with open(TIMESHEET_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, start_time, end_time, task])

def get_timesheet_data():
    timesheet_data = []
    with open(TIMESHEET_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            timesheet_data.append(row)
    return timesheet_data

def calculate_total_hours():
    total_hours = 0
    with open(TIMESHEET_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            start_time = datetime.strptime(row[1], "%H:%M")
            end_time = datetime.strptime(row[2], "%H:%M")
            time_difference = end_time - start_time
            total_hours += time_difference.total_seconds() / 3600
    return total_hours
