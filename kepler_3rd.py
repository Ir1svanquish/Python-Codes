# kepler3rd.py
# This program uses the scipy.optimize.leastsq function to determine
# the parameters alpha and beta so that the function T = alpha*a^beta
# fits the given planet data and compare them with the values predicted
# by the Kepler’s third law

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import leastsq

# Data for the motion of planets
ai = [0.38710, 0.72333, 1, 1.52366, 5.20336, 9.53707, 19.1913, 30.0690]
Ti = [87.9693, 224.701, 365.256, 686.980, 4332.82, 10775.6, 30687.2,
60190.0]
def T(a, alpha, beta):
    """ Return T(a) = alpha*a^beta """
    return alpha*a**beta

def residuals(p, Ti, ai):
    """ Compute the residuals function for the least square fitting """
    alpha, beta = p
    return Ti - T(ai, alpha, beta)

# Calculate the values of the fitting parameters predicted by
# Kepler’s 3rd law
G = 6.674e-11 # Gravitational constant in SI units
M = 1.98844e30 # Mass of the Sun in SI units
AU = 1.49598e11 # AU in meters
day = 24*60**2 # Day in seconds
# Theoretical values of alpha (in units of day/AU^1.5) and beta
alphap = np.sqrt(4*np.pi**2/(G*M))*AU**1.5/day
betap = 1.5
# Perform least squares fitting on the data
p0 = 300, 1.0
plsq = leastsq(residuals , p0, args=(Ti, ai))
alpha, beta = plsq[0]
# Compare the fitting result with the prediction by Kepler’s 3rd law
print("For least square fit with the function T = alpha*a^beta,")
print("{:>10s} {:>15s} {:>11s}".format("Parameter", "Fitting result",
"Theo value"))
print("-"*38)
print("{:>10s} {:15.5f} {:11.5f}".format("alpha", alpha, alphap))
print("{:>10s} {:15.5f} {:11.5f}".format("beta", beta, betap))
