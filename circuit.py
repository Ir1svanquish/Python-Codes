# circuit.py
# This program uses the Newton’s method to solve the simultaneous
# equations (V1 - Vp)/R1 + V1/R2 + I0(exp((V1- V2)/VT) - 1) = 0 and
# and (V2 - Vp)/R3 + V2/R4 - I0(exp((V1 - V2)/VT) - 1) = 0 to an
# accuracy of 10^(-8)V starting from the initial values V10 = 2V and
# V20 = 1V. Note that V1 and V2 are the voltages on the two sides of
# a diode in a circuit.

from math import cos, exp, sin

import numpy as np
# Set up the parameters for the simultaneous equations in SI units
R1 = 1000
R2 = 4000
R3 = 3000
R4 = 2000
Vp = 5
VT = 0.05
I0 = 3e-9

def f(x):
    """ Compute the functions f1(V1, V2) = (V1 - Vp)/R1 + V1/R2 +
        I0(exp((V1- V2)/VT) - 1) and f2(V1, V2) = (V2 - Vp)/R3 + V2/R4
        - I0(exp((V1 - V2)/VT) - 1) """
    f = np.zeros(2)
    f[0] = (x[0] - Vp)/R1 + x[0]/R2 + I0*(np.exp((x[0] - x[1])/VT) - 1)
    f[1] = (x[1] - Vp)/R3 + x[1]/R4 - I0*(np.exp((x[0] - x[1])/VT) - 1)
    return f

def dfdx(x):
    """ Compute the partial derivatives of f1(V1, V2) = (V1 - Vp)/R1 +
        V1/R2 + I0(exp((V1- V2)/VT) - 1) and f2(V1, V2) = (V2 - Vp)/R3
        + V2/R4 - I0(exp((V1 - V2)/VT) - 1) """
    dfdx = np.zeros((2, 2))
    dfdx[0,0] = 1/R1 + 1/R2 + (I0/VT)*np.exp((x[0] - x[1])/VT)
    dfdx[0,1] = -(I0/VT)*np.exp((x[0] - x[1])/VT)
    dfdx[1,0] = -(I0/VT)*np.exp((x[0] - x[1])/VT)
    dfdx[1,1] = 1/R3 + 1/R4 + (I0/VT)*np.exp((x[0] - x[1])/VT)
    return dfdx

# Use the Newton’s method to find the root of the simultaneous
# equations
x = np.array([2.0, 1.0])
delx = np.linalg.solve(dfdx(x), f(x))
tol = 1e-8
error = 1
xi = []
delxi = []
while error > tol:
    x -= delx
    xi.append(x.copy())
    delx = np.linalg.solve(dfdx(x), f(x))
    error = np.linalg.norm(delx)
    delxi.append(error)

# Output the results of computation by this method
print("{:>3s} {:>12s} {:>12s} {:>14s}".format("i", "V1i", "V2i",
                                               "||Delta(Xi)||"))
for i in range(len(xi)):
    print("{:3d} {:12.8f} {:12.8f} {:14.9f}".format(i+1, xi[i][0],
                                              xi[i][1], delxi[i]))