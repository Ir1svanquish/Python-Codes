# normal.py
# This program make a histogram of 1000 random samples drawn from the
# normal distribution with mean = 100 and standard deviation = 20 by
# using the numpy.random function normal.

import matplotlib.pyplot as plt
import numpy as np

# Draw 1000 random samples from the normal distribution
mu, sigma = 100, 20
x = np.random.normal(mu, sigma, size=1000)
# Plot the histogram of the samples
fig, ax = plt.subplots()
A = ax.hist(x, bins=50, edgecolor="k")
plt.show()
