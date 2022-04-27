# ukannualwages18.py
# This program uses Matplotlib Axes class method barh to make a
# horizontal bar chart for the average annual wages of the ten best
# paid jobs in UK in 2018

import matplotlib.pyplot as plt
import numpy as np

# Generate the data for the subplots
t = np.linspace(0, 2, 500)
A, omega, phi = 1, 10 * np.pi, np.pi/6
x = A * np.sin(omega * t + phi)
v = A * omega * np.cos(omega * t + phi)
ylab = ["x (m)", "v (m/s)"]
# Plot the subplots on the same graph with zero vertical space
# between them
fig, axes = plt.subplots(nrows=2, ncols=1)
fig.subplots_adjust(hspace=0)
for i in range(2):
    if i == 0:
        axes[i].plot(t, x, "k")
        axes[i].set_xticklabels("")
    else:
        axes[i].plot(t, v, "k")
        axes[i].set_xlabel("t (s)")
    axes[i].set_ylabel(ylab[i])
    axes[i].set_xlim(0, 2)
    axes[i].set_xticks(np.linspace(0, 2, 9))
    axes[i].tick_params(direction="in")
    axes[i].grid()
plt.suptitle("Motion of a Simple Harmonic Oscillator")
plt.show()
