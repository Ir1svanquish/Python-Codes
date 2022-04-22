# matrixprop.py
# This program uses the np.linalg module to find the determinant, rank,
# inverse, eigenvalues, and normalized eigenvectors of a matrix

import numpy as np

A = np.array([[2, -1, 0], [3, 1, 2], [-1, 1, 1]], dtype=int)
Adet = np.linalg.det(A)
Arank = np.linalg.matrix_rank(A)
Ainv = np.linalg.inv(A)
Aeigval, Aeigvec = np.linalg.eig(A)

# Display the results
print("For the matrix A =")
print(A)
print("Determinant =", Adet)
print("Rank =", Arank)
print("Inverse =")
print(Ainv)
print("{:^15s} {:^50s}".format("Eigenvalues",
"Normalized eigenvectors"))
print("-"*66)
for i in range(3):
    print("{: .4f}".format(Aeigval[i]), end=" ")
    print("[{: 4f} {: .4f} {: .4f}]".format(Aeigvec[0,i],Aeigvec[1,i],
Aeigvec[2,i]))
