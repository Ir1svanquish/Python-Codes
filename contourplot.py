# contourplot.py
# This program uses Matplotlib Axes class method contour to make a
# contour plot of the function f(x, y) = xy exp[-(x^2 + y^2)/2] over
# the region -2.5 <= x <= 2.5, -2.5 <= y <= 2.5

import matplotlib.pyplot as plt
import numpy as np
# Generate the data for the function f versus x and y
x = np.linspace(-2.5, 2.5, 100)
y = x.copy()
X, Y = np.meshgrid(x, y)
f = X * Y * np.exp(-(X ** 2+Y ** 2) / 2)
# Create the contour plot of the function f
fig = plt.figure()
ax = fig.add_subplot(111)
cp = ax.contour(X, Y, f, 15, colors = "k")
ax.clabel(cp, fontsize = 12, colors = "k")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Contour Plot of the Function f(x, y) = xyexp[-(x^2+\
y^2)/2]")
plt.show()
