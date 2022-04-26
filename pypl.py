# pypl.py
# This program uses Matplotlib Axes class method pie to draw a pie
# chart of (PYPL) Index for the programming languages worldwide released
# in Mar 2020

import matplotlib.pyplot as plt
import numpy as np
# PYPL index for the programming languages worldwide in Mar 2020
pypl = np.array([("Python", 30.09), ("Java", 18.84),
("Javascript", 8.10), ("C#", 7.27), ("PHP", 6.08),
("C/C++", 5.86), ("Others", 23.76)],
dtype=[("name", "U10"), ("index", "f4")])
# Create the contour plot of the function f
fig = plt.figure()
ax = fig.add_subplot(111)
ax.axis("equal") # So our pie looks round!
ax.pie(pypl["index"], startangle = 90, labels = pypl["name"],
autopct ="%.2f%%", pctdistance = 1.2, labeldistance = 1.35)
ax.set_title("PYPL Index for the programming languages worldwide \
in Mar 2020")
plt.show()
