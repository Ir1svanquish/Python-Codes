# vpfit.py
# This program uses the numpy.Polynomial function fit to find the best
# least-square fit of the (V, P) data of a peculiar gas to a degree-3
# polynomial in 1/V and then compare the data with the fit by plotting
# them on the same graph.

import matplotlib.pyplot as plt
import numpy as np

Polynomial = np.polynomial.Polynomial
# Fit the (V, P) data to a degree-3 polynomial in 1/V
V = [0.608, 0.430, 0.304, 0.248, 0.215, 0.192]
P = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50]
Vrec = [1.0 / i for i in V]
f = Polynomial.fit(Vrec, P, 3)
Vf = np.linspace(min(V),max(V),100)
Pf = [f(1.0 / i) for i in Vf]
fig, ax = plt.subplots()
ax.plot(V, P, "bo", label = "Data")
ax.plot(Vf, Pf, "r-", label = "Fit")
ax.set_xlabel("Volume/L")
ax.set_ylabel("Pressure/atm")
ax.legend()
plt.show()
