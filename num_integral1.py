# numintegral1.py
# This program evaluates the integral of sin x for 0 <= x <= pi using
# the trapezoidal and Simpson’s rule with different number of slices N
# and outputs a table showing the results.

from math import sin
import matplotlib.pyplot as plt
import numpy as np

from math import sin, pi
def trapezoidal(f, a, b, N):
    """ Evaluate the integral of f for a <= x <= b using the
        trapezoidal rule with N slices """
    h = (b - a)/N
    s = 0.5*(f(a) + f(b))
    for k in range(1, N):
        s += f(a+k*h)
    return s*h

def simpsons(f, a, b, N):
    """ Evaluate the integral of f for a <= x <= b using Simpson’s
        rule with N slices """
    h = (b - a)/N
    s = f(a) + f(b) + 4*f(a+(N-1)*h)
    for k in range(1, int(N/2)):
        s += 4*f(a+(2*k-1)*h) + 2*f(a+2*k*h)
    return s*h/3.0

# Evaluate the integral using the two methods with different number of
# slices N and output the results
a, b = 0, pi
Ie = 2
print("{:>4s} {:>24s} {:>24s}".format("N", "Trapezoidal (error)",
"Simpson’s (error)"))
for N in [4, 8, 16, 32, 64, 128, 256, 512, 1024]:
    It = trapezoidal(sin, a, b, N)
    Is = simpsons(sin, a, b, N)
    errt = abs(Ie - It)
    errs = abs(Ie - Is)
    print("{:4d} {:11.8f} ({:10.8f})".format(N, It, errt), end=" ")
    print("{:11.8f} ({:10.8f})".format(Is, errs))