# quadratic.py
# This program defines the class Quadratic for representing the
# quadratic function f(x) = ax^2 + bx + c.

import cmath
import math
import numpy as np

class Quadratic:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def value(self, x):
        return self.a * x ** 2+self.b * x+self.c

    def table(self, n, L, R):
        print("{:>8s} {:>8s}".format("x","f(x)"))
        for x in np.linspace(L, R, n):
            print("{:8.3f} {:8.3f}".format(x,self.value(x)))
            
    def roots(self):
        dis = (self.b) ** 2 - 4 * (self.a) * (self.c)
        denom = 2 * self.a
        if abs(dis) < 1e-8:
            return - self.b / denom, - self.b / denom
        elif dis > 0:
            sqrtdis = math.sqrt(dis)
            return (- self.b + sqrtdis) / denom, (- self.b - sqrtdis) / denom
        else:
            sqrtdis = cmath.sqrt(dis)
            return (- self.b + sqrtdis) / denom, (- self.b - sqrtdis) / denom
