# sinerror.py
# This program investigates the error of computing the the function sin(x)
# as the finite sum S(x; n).

from math import sin
import matplotlib.pyplot as plt
import numpy as np

def sinsum1(x, tol):
    """ Compute the finite sum S(x; n) that approximates sin(x) for
    given value of x with relative accuracy tol """
    sum = x
    delta = x
    n = 1
    while abs(delta/sum) > tol:
        delta *= (-1)*x**2/(2*n*(2*n+1))
        sum += delta
    n += 1
    return sum, n

def sinsum2(x, n):
    """ Compute the finite sum S(x; n) that approximates sin(x) for
    given values of x and n """
    sum = x
    delta = x
    for i in np.arange(2, n+1):
        delta *= (-1)*x**2/((2*i-1)*(2*i-2))
        sum += delta
    return sum

# Generate a table of S(x;n), n, and the relative error of computing
# sin x as S(x;n) with relative accuracy tol for different values of x
tol = 1e-7
print("{:>4s} {:>11s} {:>3s} {:>15s}".format("x", "S(x; n)", "n",
"relative error"))
for x in np.linspace(0.1,1.0,10):
    S, n = sinsum1(x, tol)
    relerror = abs((S - sin(x))/sin(x))
    print("{:4.1f} {:11.8f} {:3d} {:15.5e}".format(x, S, n, relerror))

# Plot the absolute error of computing sin x as S(x; n) vs n with log
# scaling on the y-axis for different values of x
fig, ax = plt.subplots()
xlist = list(range(1,11)) + list(range(20,51,10))
nlist = np.arange(1, 21)
for x in xlist:
    data = []
    for n in nlist:
        S = sinsum2(x, n)
        abserror = abs(S - sin(x))
        data.append(abserror)
    lab = "x = {:d}".format(x)
    ax.semilogy(nlist, data, label=lab)
ax.set_xlim(0, 20)
ax.set_xticks([0, 5, 10, 15, 20])
ax.set_xlabel("n")
ax.set_ylabel("|S(x;n) - sin(x)|")
ax.set_title("Error in computing sin x as the finite sum S(x; n)")
ax.legend()
plt.show()