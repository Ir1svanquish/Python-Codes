# pendmotion.py
# This program uses the scipy.integrate.odeint method to determine the
# subsequent motion of a pendulum of length l started at rest with an
# initial angle of theta0 = pi/6 and compare it with the approximate
# solution theta(t) = theta0*sin(sqrt(g/l)*t) for small theta.

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def dxdt(x, t, g, l):
    """ Return dx/dt = f(x,t) at time t """
    x1, x2 = x
    dx1dt = x2
    dx2dt = -(g/l)*np.sin(x1)
    return dx1dt, dx2dt

g, l = 9.81, 1
omega = np.sqrt(g/l)
x0 = np.pi/6, 0
t = np.linspace(0, 8, 200)

# Integrate the DE to obtain the numerical solution
x1, x2 = odeint(dxdt, x0, t, args=(g,l)).T

# Plot the numerical solutions
fig, ax = plt.subplots()
ax.plot(t, x1, "x", color="b", label="Exact solution")
ax.plot(t, x0[0]*np.cos(omega*t), "-", color="r",
label="Small angle solution" )
ax.set_xlabel(r"$t/\mathrm{s}$")
ax.set_ylabel(r"$\theta(t)/\mathrm{rad}$")
ax.set_xlim(0, 8)
ax.set_ylim(-0.7, 0.7)
ax.set_title("Motion of a pendulum")
ax.legend(loc="lower center")
ax.grid()
plt.show()
