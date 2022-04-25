# numintegral3.py
# This program uses the adaptive Simpson’s rule to compute the value of
# the integral of sin^2(sqrt(100x)) for 0 <= x <= 1 to an accuracy of
# 1e-8 with an initial number of slices of 10 and then output the value
# of the integral and the number of slices used to get the result.

from math import sin, sqrt

def f(x):
    """ Compute the function f(x) = sin^2(sqrt(100x)) """
    return sin(sqrt(100*x))**2

def adpSimpsons(f, a, b, N, tol):
    """ Evaluate the integral of f for a <= x <= b using the adaptive
        Simpson’s rule with an accuracy of tol and an initial number
    of slices of N """
    error = 1
    h = (b - a)/N
    So = f(a) + f(b)
    To = f(a + h)
    for k in range(2, N, 2):
        So += 2 * f(a + k * h)
        To += f(a + (k + 1) * h)
    So /= 3.0
    To *= 2.0 / 3.0
    Io = h * (So + 2 * To)
    while abs(error) > tol:
        N *= 2
        h *= 0.5
        Sc = So + To
        Tc = 0
        for k in range(1, N, 2):
            Tc += f(a + k * h)
        Tc *= 2.0 / 3.0
        Ic = h * (Sc + 2 * Tc)
        error = (Ic - Io) / 15.0
        So, To, Io = Sc, Tc, Ic
    return Ic, N

# Use the adaptive Simpson’s rule to compute the integral and output
# the result
a, b = 0, 1
tol = 1e-8
N = 10
I, N = adpSimpsons(f, a, b, N, tol)
print("Using the adaptive Simpson’s rule to compute the integral of")
print("sin^2(sqrt(100x)) for 0 <= x <= 1 to an accuracy of 1e-8 with")
print("an initial number of slices of 10, we find that:")
print(" value of the integral = {:.8f},".format(I), end="")
print(" number of slices used =", N)