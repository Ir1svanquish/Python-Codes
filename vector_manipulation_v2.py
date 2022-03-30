# Vector Manipulation
# Version 2

# Input two vectors of the same length and store them as lists
while True:
    strA = input('Enter the vector A: ')
    strB = input('Enter the vector B: ')
    strA = strA.strip('[]')
    strB = strB.strip('[]')
    lstA = strA.split(', ')
    lstB = strB.split(', ')

    if len(lstA) == len(lstB):
        A = [int(i) for i in lstA]
        B = [int(i) for i in lstB]
        break
    print('Invalid input! Vectors A and B must have the same length.')

# Compute the sum, difference, and dot product of these two vectors by
# manipulating the lists storing them
AplusB = [A[i]+B[i] for i in range(len(A))]
AminusB = [A[i]-B[i] for i in range(len(A))]
AdotB = sum([A[i]*B[i] for i in range(len(A))])

# Output the results
print('A+B =', AplusB)
print('A-B =', AminusB)
print('A.B =', AdotB)
