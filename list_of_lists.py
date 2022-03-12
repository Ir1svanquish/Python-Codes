# list_of_lists.py
# This program generates a list of lists of the form [[n], [n - 1, n],
# [n - 2, n - 1, n], ..., [1, 2, ..., n]] for a positive integer n.

n = int(input("Enter a positive integer: "))
available = 1

if n <= 0:
    print("Invalid input")
    available = 0

if available == 1:
    lsto = []
    for i in range(n, 0, -1):
        lsti = []
        for j in range(i, n + 1):
            lsti.append(j)
        lsto.append(lsti)
    print(lsto)
