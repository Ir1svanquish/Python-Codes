# complex_number.py
# This program produces the exponential of a complex number and represents it
# in polar coordinates.

from cmath import exp, polar
c = complex(input("Enter a complex number: "))
print(exp(c))
print(polar(c))
