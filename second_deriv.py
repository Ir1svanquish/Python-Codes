# secondderiv.py
# This program computes the second-order derivative of the function
# f(x) = cos(x)*sinh(x) at 51 uniformly spaced points for 0 <= x <=
# pi/2 using the central difference based only on the values of f(x)
# at 53 uniformly spaced points for -pi/100 <= x <= 51pi/100. It then
# outputs a table of the derivative with its error for different
# values of x.

from math import cos, sin, cosh, sinh, pi
import numpy as np

def f(x):
    """ Compute the function f(x) = cos(x)*sinh(x) """
    return cos(x)*sinh(x)

def cdiff(f, x, h):
    """ Compute the second-order derivative of f(x) using the central
        difference with step size h """
    return (f(x + h) - 2*f(x) + f(x - h))/h**2

# Compute the second-order derivative of f(x) = cos(x) sinh(x) using
# the central difference and output a table of the derivative with its
# error for different values of x
a, b = 0, 0.5
N = 51
h = (b-a)*pi/(N-1)
print("[Second-order derivative of f(x) = cos(x)*sinh(x)")
print("computed by the central difference]")
print("{:>6s} {:>12s} {:>12s}".format("x", "f”(x)", "Error"))
for i in np.linspace(a, b, N):
    x = i*pi
    fppc = cdiff(f, x, h)
    efppc = abs(fppc + 2*sin(x)*cosh(x))
    print("{:.2f}pi {:12.8f} {:12.8f}".format(i, fppc, efppc))