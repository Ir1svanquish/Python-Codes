# newtons.py
# This program uses the Newton’s method to find a root of f(x) =
# 2*sin(3x) - exp(x) to an accuracy of 10^(-12) starting from the
# initial value x0 = 0.

from math import cos, exp, sin

def f(x):
    """ Compute the function f(x) = 2*sin(3x) - exp(x) """
    return 2*sin(3*x) - exp(x)

def dfdx(x):
    """ Compute the derivative of f(x) = 2*sin(3x) - exp(x) """
    return 6*cos(3*x) - exp(x)

# Use the Newton’s method to find the root of f(x)
x = 0
delx = f(x)/dfdx(x)
tol = 1e-12
error = 1
xi = []
errxi = []
while error > tol: # Error of x i = x (i+1) - x i!!
    x -= delx
    xi.append(x)
    delx = f(x)/dfdx(x)
    error = abs(delx)
    errxi.append(error)

# Output the results of computation by this method
print("{:>3s} {:>16s} {:>17s}".format("i", "xi", "|Error(xi)|"))
for i in range(len(xi)):
    print("{:3d} {:16.12f} {:17.13f}".format(i+1, xi[i], errxi[i]))