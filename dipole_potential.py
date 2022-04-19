# dipolepotential.py
# This program uses the Matplotlib module to make the surface plot of
# the electric potential V(x, y) due to an electric dipole over the
# region -0.1m <= x <= 0.1m, -0.1m <= y <= 0.1m.

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Generate the data for the electric potential V versus x and y
k, q, d = 8.99e9, 5e-9, 0.001
x = np.linspace(-0.01, 0.01, 50)
y = x.copy()
X, Y = np.meshgrid(x, y)
V = k*q*(1/np.sqrt((X - d)**2 + Y**2) - 1/np.sqrt((X + d)**2 + Y**2))

# Create the surface plot of the electric potential V
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X/0.001, Y/0.001, V/1000)
ax.set_xlabel("x/mm")
ax.set_ylabel("y/mm")
ax.set_zlabel("V(x, y)/kV")
ax.set_title("Electric Potential due to an Electric Dipole")
plt.show()
