# spacecurve.py
# This program uses the matplotlib module to plot the space curve
# defined by the parametric equations x(t) = e^(t/4) cos 2t, y(t) =
# e^(t/4) sin 2t, z(t) = t for 0 <= t <= 15.

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Generate the data for the electric potential V versus x and y
k, q, d = 8.99e9, 5e-9, 0.001
x = np.linspace(-0.01, 0.01, 50)
y = x.copy()
X, Y = np.meshgrid(x, y)
V = k*q*(1/np.sqrt((X - d)**2 + Y**2) - 1/np.sqrt((X + d)**2 + Y**2))

# Generate the points of the space curve
t = np.linspace(0, 15, 500)
x = np.exp(t/4)*np.cos(2*t)
y = np.exp(t/4)*np.sin(2*t)
z = t

# Create the plot of the space curve
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(x, y, z, "b")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_title("The space curve x(t) = e^(t/4)cos2t, \
y(t) = e^(t/4)sin2t, z(t) = t")
plt.show()
