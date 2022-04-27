# sphericaltank.py
# This program uses NumPy Polynomial class to find the height of the
# liquid in a spherical tank of radius R (in m) from which liquid is
# being drawn at a constant rate F (in m^3/s). Assume the process
# starts with a full tank at time t, i.e. h(0) = 2R

import matplotlib.pyplot as plt
import numpy as np
Polynomial = np.polynomial.Polynomial

R, F = 1.5, 2.e-4
V0 = 4/3 * np.pi * R ** 3
# Total time taken for the tank to empty
T = V0/F
# Coefficients of the quadratic and cubic terms of p(h), the
# polynomial to be solved for h
c2, c3 = np.pi * R, -np.pi/3
# Solve p(h) = 0 to find the value of h from time t = 0 to T
N = 100
time = np.linspace(0, T, N)
h = np.ones(N) * 2 * R
for i, t in enumerate(time[1:]):
    c0 = F * t - V0
    p = Polynomial([c0, 0, c2, c3])
    roots = p.roots()
# We take the one root for which 0 <= h <= 2R
    h[i + 1] = roots[(0 <= roots) & (roots <= 2 * R)][0]
fig, ax = plt.subplots()
ax.plot(time, h, "o")
ax.set_xlabel("Time t/s")
ax.set_ylabel("Height of the liquid in the tank h(t)/m")
plt.show()
