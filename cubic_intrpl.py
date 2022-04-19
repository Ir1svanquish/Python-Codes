# cubicintrpl.py
# This program uses the scipy.interpolate.interp1d function to perform
# cubic spline interpolation on the data ponts of the function f(x) =
# 6.4sin(pi*x/15) and plot the interpolation result and the "exact"
# values given by f(x) on the same graph.

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

def f(x):
    """ Return f(x) = 6.4sin(pi*x/15) """
    return 6.4*np.sin(np.pi*x/15.0)

# Perform the cubic spline interpolation on the given data
x = [0.15, 1.45, 2.30, 3.15, 4.85, 5.65, 6.25, 7.95]
y = [0.2010, 1.9139, 2.9651, 3.9226, 5.4393, 5.9256, 6.1819, 6.3716]
fc = interp1d(x, y, kind="cubic")

# Plot the interpolation result and the "exact" values given by f(x)
fig, ax = plt.subplots()
xc = np.linspace(min(x), max(x), 100)
ax.plot(x, y, "o", label="Data points")
ax.plot(xc, f(xc), color="b", label="Exact")
ax.plot(xc, fc(xc), linestyle="-", color="r", label="Cubic spline")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$f(x)$")
ax.set_title(r"Interpolation for the data points of $f(x)$ = " +
r"6.4sin$(\pi x/10)$")
ax.legend()
plt.show()
