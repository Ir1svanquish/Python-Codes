# bisection.py
# This program uses the bisection method to find a root of f(x) =
# x*tan(x) - sqrt(100 - x^2) on the interval 6.5 <= x <= 7.5 to an
# accuracy of 10^(-12).

from math import sqrt, tan

def f(x):
    """ Compute the function f(x) = x*tan(x) - sqrt(100 - x^2) """
    return x*tan(x) - sqrt(100 - x**2)
a, b = 6.5, 7.5
if f(a)*f(b) > 0:
    print("Bisection method fails for this case!")
else:
    # Use the bisection method to find the root of f(x)
    x1, x2 = a, b
    tol = 1e-12
    error = 1
    xm = a
    xi = []
    delxi = []
    
while error > tol:
    xmo = xm
    xm = 0.5*(x1 + x2)
    if f(xm) * f(x1) > 0:
        x1 = xm
    else:
        x2 = xm
    error = abs(x1 - x2)
    xi.append(xm)
    delxi.append(abs(xm - xmo))
    xmo = xm
    xm = 0.5 * (x1 + x2)
    xi.append(xm)
    delxi.append(abs(xm - xmo))

    # Output the results of computation by this method
    print("{:>3s} {:>16s} {:>17s}".format("i", "x i", "|x i - x (i-1)|"))
    print("{:3d} {:16.12f} {:>17s}".format(1, xi[0], "n/a"))
    for i in range(1, len(xi)):
        print("{:3d} {:16.12f} {:17.13f}".format(i + 1, xi[i], delxi[i]))