# relaxationsimeq.py
# This program uses the relaxation method to solve the simultaneous
# equations x^2 - 2x + y^4 - 2y^2 + y = 0 and x^2 + x + 2y^3 - 2y^2
# - 1.5y - 0.05 = 0 starting from the initial values x = 0 and y = 1.
# It outputs each successive estimate of x and y until they both have
# absolute change less than 10^(-10).

from math import cos, exp, sin

from math import exp, log
def f(x):
    """ Compute the function f(x) = exp(x^2)*ln(x^2) - x """
    return exp(x**2)*log(x**2) - x

# Use the relaxation method to find the root of the simultaneous
# equations
x = 0
y = 1
tol = 1e-10
delx = dely = 1
xi = []
yi = []
while delx > tol or dely > tol:
    xo = x
    yo = y
    x = (xo**2 + yo**4 - 2*yo**2 + yo)/2.0
    y = (xo**2 + xo + 2*yo**3 - 2*yo**2 - 0.05)/1.5
    delx = abs(x - xo)
    dely = abs(y - yo)
    xi.append(x)
    yi.append(y)

# Output the results of computation by this method
print("{:>3s} {:>14s} {:>14s}".format("i", "xi", "yi"))
for i in range(len(xi)):
    print("{:3d} {:14.10f} {:14.10f}".format(i+1, xi[i], yi[i]))