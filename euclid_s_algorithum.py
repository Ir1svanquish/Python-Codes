"""

Euclid's algorithm

"""
a = int(input())
b = int(input())

if b > a:
    a, b = b, a
while a != b:
    a, b = a - b, b
    if b > a:
        a, b = b, a
print('(%d , %d)' % (a, b))
