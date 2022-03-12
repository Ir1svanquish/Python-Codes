# datetime.py
# This program produces the current day and time

from datetime import datetime
print("Today is", datetime.now().strftime("%Y-%m-%d"))
print("Current time is", datetime.now().strftime("%H:%M:%S"))
