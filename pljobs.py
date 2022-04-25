# pljobs.py
# This program uses Matplotlib Axes class method scatter to make a
# scatter plot of the job openings versus the TIOBE index in USA in Jan
# 2020 according to Indeed.com for the ten most in-demand programming
# languages with marker area proportional to the average year salary

import matplotlib.pyplot as plt
import numpy as np
# Name of programming languages
pl = ["Python", "Java", "Javascript", "C++", "C#", "C", "PHP", "Ruby",
"Swift", "Go"]
# Job openings in K
jobs = [74, 69, 57, 41, 32, 28, 18, 16, 6, 4]
# Average year salary in thousand US dollars
salary = np.array([120, 104, 114, 108, 96, 104, 90, 134, 125, 93])
# TIOBE index in %
tiobe = [9.704, 16.896, 2.451, 5.574, 5.349, 15.773, 2.405, 1.063,
1.795, 0.900]
# Create the scatter plot of the data for the programming languages
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(tiobe, jobs, c = range(len(pl)), s = salary / 2)
ax.set_xlabel("TIOBE index (%)")
ax.set_ylabel("Job Openings on Indeed.com (K)")
ax.set_title("Most In-demand Programming Languages in USA (Jan 2020)")
plt.show()
