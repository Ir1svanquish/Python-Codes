# ukannualwages18.py
# This program uses Matplotlib Axes class method barh to make a
# horizontal bar chart for the average annual wages of the ten best
# paid jobs in UK in 2018

import matplotlib.pyplot as plt
import numpy as np

# Job title
jobtitle = ["CEOs", "Medical practitioners",
"Marketing sales directors",
"IT & telecommunications directors",
"Legal professionals", "Financial managers",
"Advertising & PR directors",
"Senior police officers", "Functional managers",
"Train/tram drivers"]
# Average annual wages in UK pounds
annualwages = np.array([97083, 75855, 75126, 72109, 69992, 67593,
65074, 59634, 57098, 53403])

# Create the bar chart of the average annual wages
fig = plt.figure()
ax = fig.add_subplot(111)
y = 10-np.arange(len(jobtitle))
ax.barh(y, annualwages/1000, color="gray", align="center")
ax.set_yticks(y)
ax.set_yticklabels(jobtitle)
ax.tick_params(axis="x", direction="out")
ax.set_xlim(0, 100)
ax.xaxis.grid(True)
ax.set_xlabel("Average annual wages (in 1000 UK pounds)")
plt.suptitle("Average Annual Wages of the Ten Best Paid Jobs in UK \
in 2018")
plt.show()
