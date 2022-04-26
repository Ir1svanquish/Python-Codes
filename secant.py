# secant.py
# This program uses the Secant method to find a root of f(x) =
# exp(x^2)*ln(x^2) - x to an accuracy of 10^(-12) starting from the
# initial values x0 = 1 and x1 = 2.

from math import cos, exp, sin

from math import exp, log
def f(x):
    """ Compute the function f(x) = exp(x^2)*ln(x^2) - x """
    return exp(x**2)*log(x**2) - x

# Use the Secant method to find the root of f(x)
xo, x = 1, 2
delx = f(x)*(x - xo)/(f(x) - f(xo))
tol = 1e-12
error = 1
xi = []
errxi = []
while error > tol: # Error of x i = x (i+1) - x i!!
    xo = x
    x -= delx
    xi.append(x)
    delx = f(x)*(x - xo)/(f(x) - f(xo))
    error = abs(delx)
    errxi.append(error)
# Output the results of computation by this method
print("{:>3s} {:>16s} {:>17s}".format("i", "xi", "|Error(xi)|"))
for i in range(len(xi)):
    print("{:3d} {:16.12f} {:17.13f}".format(i+2, xi[i], errxi[i]))