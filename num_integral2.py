# numintegral2.py
# This program evaluates the integral of exp(-x) for 0 <= x <= 1 using
# the trapezoidal and Simpson’s rule with different number of slices N
# and make a log-log plot of the relative error of the integral versus
# the number of slices N in each case.

from math import exp
import matplotlib.pyplot as plt

def f(x):
    """ Compute the function f(x) = exp(-x) """
    return exp(-x)

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
        with N slices """
    h = (b - a)/N
    s = f(a) + f(b) + 4*f(a+(N-1)*h)
    for k in range(1, int(N/2)):
        s += 4*f(a+(2*k-1)*h) + 2*f(a+2*k*h)
    return s*h/3.0

# Evaluate the integral using the two methods with different N
a, b = 0, 1
Ie = 1.0 - exp(-1.0)
Nlist = [i**2 for i in range(2, 82, 2)]
relerrort = []
relerrors = []
for N in Nlist:
    It = trapezoidal(f, a, b, N)
    Is = simpsons(f, a, b, N)
    relerrort.append(abs(Ie - It)/Ie)
    relerrors.append(abs(Ie - Is)/Ie)
# Make a log-log plot of the relative error of the integrals vs N
fig, ax = plt.subplots()
ax.loglog(Nlist, relerrort, label="Trapezoidal")
ax.loglog(Nlist, relerrors, label="Simpson’s")
ax.set_xlabel(r"Number of Slices $N$")
ax.set_ylabel(r"Relative Error $\epsilon$")
ax.set_title("Errors in the numerical integrals of exp(-x) from x = \
0 to x = 1")
ax.legend()
plt.show()