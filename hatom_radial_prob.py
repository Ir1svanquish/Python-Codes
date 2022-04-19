# hatomradialprob.py
# This program uses the scipy.special package to plot the radial prob.
# density P(r) versus r/a 0 from r = 0 to r = 30a 0 for the case n = 3
# and ell = 1.

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import eval_genlaguerre

# Generate the data points for the P(r) vs r curve
n, ell = 3, 1
r = np.linspace(0, 30, 100)
A = (2/n)**3*math.factorial(n-ell-1)/(2*n*math.factorial(n+ell))
rho = 2*r/n
P = A*r**2*np.exp(-rho)*(rho)**(2*ell)\
*(eval_genlaguerre(n-ell-1,2*ell+1,rho)**2)

# Plot the P(r) vs r curve
fig, ax = plt.subplots()
ax.plot(r, P)
ax.set_xlim(0, 30)
ax.set_ylim(0)
ax.set_xlabel(r"$r/a 0$")
ax.set_ylabel(r"$P(r)/(1/a 0)$")
title = r"Radial probability density of H-atom for n = 3 and $\ell$ = 1"
ax.set_title(title)
plt.show()
