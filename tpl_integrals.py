# tplintegrals.py
# This program uses the SciPy method tplquad to evaluate two triple
# integrals.

import numpy as np
from scipy.integrate import tplquad

# Evaluate the first integral
def func1(z, y, x):
    """ Compute the function 6xyz """
    return 6*x*y*z

def rfun1(x, y):
    """ Compute the function sqrt(1 - y^2) """
    return np.sqrt(1 - y**2)

I1 = tplquad(func1, 0, np.pi, 0, 1, 0, rfun1)
print("The first integral is {:f}.".format(I1[0]))

# Evaluate the second integral
def func2(r, theta, phi):
    """ Compute the function r^2*sin(theta) """
    return r**2*np.sin(theta)

def rfun2(phi, theta):
    """ Compute the function 2/cos(theta) """
    return 2/np.cos(theta)

I2 = tplquad(func2, 0, 2*np.pi, 0, np.pi/4, 0, rfun2)
print("The second integral is {:f}.".format(I2[0]))
