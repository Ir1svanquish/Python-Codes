# planckslaw.py
# This program evalautes the integral in Planck’s law of thermal
# radiation using Simpson’s rule with 100 slices and then uses this
# integral to compute the value of the Stefan-Boltzmann constant.

from math import sin, sqrt

def f(x):
    """ Compute the function f(x) = sin^2(sqrt(100x)) """
    return sin(sqrt(100*x))**2

def trapezoidal(f, a, b, N):
    """ Evaluate the integral of f for a <= x <= b using the
        trapezoidal rule with N slices """
    h = (b - a)/N
    s = 0.5*(f(a) + f(b))
    for k in range(1, N):
        s += f(a+k*h)
    return s*h

def romberg(f, a, b, N, tol):
    """ Evaluate the integral of f for a <= x <= b using the Romberg
        integration with an accuracy of tol and an initial number of
        slices of N """
    R = [[trapezoidal(f, a, b, N)]] # Note that R[i-1][m-1] = R {i, m}
    i = 2
    flag = 0
    while (flag == 0):
        R.append([0 for j in range(1,i+1)])
        N *= 2
        for m in range(i-1):
            if m == 0:
                R[i-1][m] = trapezoidal(f, a, b, N)
            else:
                R[i-1][m] = R[i-1][m-1] + (R[i-1][m-1] -
                                           R[i-2][m-1])/(4**m - 1)
            error = abs((R[i-1][m] - R[i-2][m])/(4**(m+1) - 1))
            if error <= tol:
                flag = 1
                break
        if flag != 1:
            R[i-1][i-1] = R[i-1][i-2] + (R[i-1][i-2] -
                                         R[i-2][i-2])/(4**(i-1) - 1)
            i += 1
    return R

# Evaluate the Romberg estimates of the integral and output the result
a, b = 0, 1
N = 10
tol = 1e-8
R = romberg(f, a, b, N, tol)
m = len(R)
print("Using the Romberg integration to compute the integral of")
print("sin^2(sqrt(100x)) for 0 <= x <= 1 to an accuracy of 1e-8")
print("with an initial number of slices of 10, we find that the")
print("Romberg estimates of the integral are:")
print("I1 = {:10.8f}".format(R[0][0]))
for i in range(1,m):
    print("{:>15s} {:>1s}".format("", "\u2198"), end="")
    for j in range(i-1):
        print("{:>13s}".format("\u2198"), end="")
    print()
    print("I{0:1d} = {1:10.8f}".format(i+1, R[i][0]), end="")
    for j in range(1, i+1):
        if R[i][j] != 0:
            print("{:>2s} {:10.8f}".format("\u2192", R[i][j]), end="")
        else:
            print("{:>2s} {:10s}".format("\u2192", "-"*10), end="")
    print()