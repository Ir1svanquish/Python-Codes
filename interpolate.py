# interpolate.py
# This program performs linear interpolation on the given data of
# f(x) = exp(sin(x)) at several points to find its values at x = 0.1,
# 0.2, 0.3, ..., 4.9 and then plot the interpolated values and exact
# values of f(x) as well as the data for interpolation versus x for
# 0 <= x <= 5 on the same graph.

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    """ Compute the function f(x) = exp(sin(x)) """
    return np.exp(np.sin(x))

def interpolate(fa, fb, a, b, x):
    """ Compute the interpolated value of f(x) at x from its value at
        x = a and x = b """
    return ((b-x)*fa + (x-a)*fb)/(b-a)

# Given data for performing interpolation
xd = [0, 0.36, 1.22, 2.15, 2.78, 3.62, 4.27, 5]
fxd = [1, 1.42229, 2.55768, 2.30919, 1.42442, 0.63105, 0.40505,
0.38331]
# Perform linear interpolation on the given data to find the values of
# f(x) at x = 0.1, 0.2, 0.3, ..., 4.9
xi = np.arange(0, 5.1, 0.1)
fxi = [fxd[0]]
i = 0
for x in xi[1:-1]:
    if x == xd[i+1]:
        fxi.append(fxd[i+1])
    else:
        while x > xd[i+1]:
            i += 1
        fxi.append(interpolate(fxd[i], fxd[i+1], xd[i], xd[i+1], x))
fxi.append(fxd[-1])

# Plot the interpolated values and the exact values of f(x) as well as
# the data for interpolation vs x for 0 <= x <= 5 on the same graph
fig, ax = plt.subplots()
ax.plot(xi, f(xi), "b-", label="Exact values")
ax.plot(xd, fxd, "kx", label="Data for interpolation")
ax.plot(xi, fxi, "r-", label="Interpolated values")
ax.set_xlim(-0.5, 5.5)
ax.set_xlabel("_x")
ax.set_ylabel("f(x)")
ax.set_title("Linear Interpolation of f(x) = exp(sin(x))")
ax.legend()
plt.show()