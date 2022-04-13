# blackbody.py
# This program finds the best least-square fit of the data of the total
# intensity I emitted by a blackbody weighted by the inverse square of
# the error for the measurement of I to a degree-4 polynomial of its
# temperature T by using the numpy.Polynomial function fit and plot the
# fitting result as a line and the data as points with error bars on the
# same graph by using the matplotlib module.

import matplotlib.pyplot as plt
import numpy as np

Polynomial = np.polynomial.Polynomial
# Temperature of the blackbody
T = np.array([300, 350, 400, 450, 500, 550, 600])
# Total intensity radiated by the blackbody
I = np.array([431.0, 780.2, 1415.4, 2327.3, 3225.0, 5400.9, 7295.5])
# Error in the measured value of the intensity
Ierr = np.array([45.6, 85.0, 77.4, 153.3, 310.8, 464.6, 379.8])
# Fit the data to a degree-4 polynomial in T and generate the fitting
# result for plotting
f = Polynomial.fit(T, I, 4, w=Ierr**(-2))
Tf = np.linspace(min(T),max(T),100)
If = f(Tf)
# Make the plot of the fitting result and the data on the same graph
fig = plt.figure()
ax = fig.add_subplot(111)
ax.errorbar(T, I, yerr=Ierr, marker="o", ls="", color="r", label="Data")
ax.plot(Tf, If, ls="-", color="b", label="Fit")
ax.set_xlabel("Temperature T (K)")
ax.set_ylabel("Intensity I (W/m^2)")
ax.set_ylim(0, 8000)
ax.set_title("Total Intensity I Emitted by a Blackbody Versus its \
Temperature T")
ax.grid()
ax.legend()
plt.show()
