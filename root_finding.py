# rootfinding.py
# This program plots the function f(x) = 1/5 + x*sin(3/x) for
# -2 <= x <= 2 and then uses the functions scipy.optimize.brentq and
# scipy.optimize.newton to find all its roots

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq, newton

def f(x):
    """ Return f(x) = 1/5 + x*sin(3/x) """
    return 0.2 + x*np.sin(3.0/x)

def fp(x):
    """ Return f’(x) = sin(3/x) - (3/x)*cos(3/x) """
    return np.sin(3.0/x) - (3.0/x)*np.cos(3.0/x)

# Plot the function f(x)
x = np.linspace(-2, 2, 1000)
fig, ax = plt.subplots()
ax.plot(x, f(x), "-", color="b")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$f(x)$")
ax.set_xlim(-2, 2)
ax.set_title(r"Plot of the $f(x)$ = 1/5 + $x$sin($3/x$)")
ax.grid()
plt.show()

# Find all the roots of f(x) using different functions
rootint = [[-1.0, -0.8], [-0.6, -0.4], [-0.3, -0.27], [-0.27, -0.2],
[0.2, 0.27], [0.27, 0.3], [0.4, 0.6], [0.8, 1.0]]
print("Using the scipy.optimize.brentq function,")
print("{:>13s} {:>9s}".format("Interval", "Root"))
print("="*23)
for i in range(len(rootint)):
    rb = brentq(f, rootint[i][0], rootint[i][1])
    print("{:>13s} {:9.5f}".format(str(rootint[i]), rb))
print()
x0 = [-1.0, -0.6, -0.3, -0.27, 0.27, 0.3, 0.6, 1.0]
print("Using the scipy.optimize.newton function,")
print("{:>13s} {:>9s}".format("Initial guess", "Root"))
print("="*23)
for i in range(len(x0)):
    rn = newton(f, x0[i], fprime=fp)
    print("{:>13s} {:9.5f}".format(str(x0[i]), rn))
