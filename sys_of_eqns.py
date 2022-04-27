# sysofeqns.py
# This program uses the np.linalg module to find & print the solutions
# of some systems of equations.

import numpy as np
# Construct the matrices and vectors for the systems of equations
A1 = np.array([[-3, -2, 4], [0, 3, -2], [4, -3, 2]], dtype=int)
b1 = np.array([9, 5, 7], dtype=int)
A2 = np.array([[1, 1, 1, 1], [1, 2, 3, 4], [1, 3, 6, 10],
[1, 4, 10, 20]], dtype=int)
b2 = np.array([4, 10, 20, 35], dtype=int)
# Solve the systems of equations and display the results
x1 = np.linalg.solve(A1, b1)
x2 = np.linalg.solve(A2, b2)
print("For the matrix A =")
print(A1)
print("and the vector b = {:},".format(b1))
print("the solution of the equation Ax = b is", x1)
print("")
print("For the matrix A =")
print(A2)
print("and the vector b = {:},".format(b2))
print("the solution of the equation Ax = b is", x2)
