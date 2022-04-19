# firstderiv.py
# This program computes the first-order derivative of the function f(x)
# = cos(x) at 9 uniformly spaced points for 0 <= x <= pi using different
# methods based only on the values of f(x) at 11 uniformly spaced points
# for -pi/8 <= x <= 9pi/8. Then it outputs a table of each derivative
# with its error for different values of x.

from math import cos, sin, pi
import numpy as np

def fdiff(f, x, h):
    """ Compute the first-order derivative of f(x) using the forward
        difference with step size h """
    return (f(x + h) - f(x))/h

def bdiff(f, x, h):
    """ Compute the first-order derivative of f(x) using the backward
        difference with step size h """
    return (f(x) - f(x - h))/h

def cdiff(f, x, h):
    """ Compute the first-order derivative of f(x) using the central
        difference with step size h """
    return 0.5*(f(x + h) - f(x - h))/h

# Compute the first-order derivative of f(x) = cos(x) using different
# methods and output a table of each derivative with its error for
# different values of x
a, b = 0, 1
N = 9
h = (b-a)*pi/(N-1)
print("[First-order derivative of f(x) = cos(x) computed by different \
methods]")
print("{:>7s} {:>21s} {:>22s}".format("x", "Forward diff (error)",
"Backward diff (error)"), end="")
print("{:>21s}".format("Central diff (error)"))
for i in np.linspace(a, b, N):
    x = i*pi
    fpf = fdiff(cos, x, h)
    fpb = bdiff(cos, x, h)
    fpc = cdiff(cos, x, h)
    efpf = abs(fpf + sin(x))
    efpb = abs(fpb + sin(x))
    efpc = abs(fpc + sin(x))
    print("{:5.3f}pi {:11.5f} ({:.5f})".format(i, fpf, efpf), end=" ")
    print("{:12.5f} ({:.5f}) {:11.5f} ({:.5f})".format(fpb, efpb,
                                                       fpc, efpc))