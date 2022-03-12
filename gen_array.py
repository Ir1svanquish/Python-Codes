# gen_array.py
# This program takes two digits m and n as input and generates a mxn
# array where the element in the i-th row and j-th column of the
# array is i*j with i = 1, 2, ..., m and j = 1, 2, ..., n.

import numpy as np
available = 1

m = int(input("Enter the number of rows (< 10): "))
if (m <= 0) and (m >= 10):
    print("Invalid input")
    available = 0

n = int(input("Enter the number of columns (< 10): "))
if (n <= 0) and (n >= 10):
    print("Invalid input")
    available = 0

if (available == 1):
    a = np.zeros((m, n), dtype = int)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            a[i - 1, j - 1] = i * j
print(a)
