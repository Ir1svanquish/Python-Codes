# rational_number.py
# This program defines the class RationalNumber for representing
# rational numbers.

def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)

class RationalNumber:
    def __init__(self, num, den):
        g = gcd(abs(num), abs(den))
        self.num = int(num / g)
        self.den = int(den / g)
        
    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return RationalNumber(num, den)

    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return RationalNumber(num, den)

    def __mul__(self, other):
        return RationalNumber(self.num * other.num, self.den * other.den)
    
    def __truediv__(self, other):
        return RationalNumber(self.num * other.den, self.den * other.num)
    
    def display(self):
        print("{:s}/{:s}".format(str(self.num), str(self.den)))
