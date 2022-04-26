# relaxationvar.py
# This program uses the relaxation method to find a solution of x =
# f(x) = exp(exp(-x)*cos(x)) to an accuracy of 10^(-12) starting from
# the initial value x0 = 1 without using the formula of f’(x).

from math import cos, exp

def f(x):
    """ Compute the function f(x) = exp(exp(-x)*cos(x)) """
    return exp(exp(-x)*cos(x))

# Use the relaxation method to find the solution of x = f(x) without
# using the formula of f’(x)
xo = 1
x = f(xo)
tol = 1e-12
error = 1
xi = [x]
errxi = [error]
while error > tol:
    xoo = xo
    xo = x
    x = f(xo)
    error = abs((xo - x)**2/(2*xo - xoo - x))
    xi.append(x)
    errxi.append(error)
# Output the results of computation by this method
print("{:>3s} {:>16s} {:>17s}".format("i", "xi", "|Error(xi)|"))
print("{:3d} {:16.12f} {:>17s}".format(1, xi[0], "n/a"))
for i in range(1, len(xi)):
    print("{:3d} {:16.12f} {:17.13f}".format(i+1, xi[i], errxi[i]))