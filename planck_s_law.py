# planckslaw.py
# This program evalautes the integral in Planck’s law of thermal
# radiation using Simpson’s rule with 100 slices and then uses this
# integral to compute the value of the Stefan-Boltzmann constant.


from math import exp, isclose, pi
from scipy.constants import c, h, k, sigma

def f(z):
    """ Compute the function f(x) = x^3/(exp(x) - 1) with the
        change of variable z = x/(1 + x) """
    if isclose(z, 0) or isclose(z, 1):
        return 0
    x = z/(1 - z)
    return (x**3/(exp(x) - 1))/(1 - z)**2

def simpsons(f, a, b, N):
    """ Evaluate the integral of f for a <= x <= b using Simpson’s
        rule with N slices """
    h = (b - a)/N
    s = f(a) + f(b) + 4*f(a+(N-1)*h)
    for k in range(1, int(N/2)):
        s += 4*f(a+(2*k-1)*h) + 2*f(a+2*k*h)
    return s*h/3.0

# Evaluate the integral in Planck’s law of thermal radiation using
# Simpson’s rule and then uses this integral to compute the value of
# of the Stefan-Boltzmann constant
a, b = 0, 1
N = 100 # Too big N will lead to overflow due to exp(x) term in f!
I = simpsons(f, a, b, N)
sigmaI = 2*pi*k**4*I/(c**2*h**3)

# Output the result with its theoretical value
print("Using the value of the integral in Planck’s law of thermal \
radiation")
print("computed by Simpson’s rule with 100 slices, we find that:")
print(" Stefan-Boltzmann constant = {:.8e},".format(sigmaI))
print(" its theoretical value = {:.8e}.".format(sigma))