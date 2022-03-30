# Bubble Sort
# Version 2

# Import the randint function from the random module
from random import randint
# Generate a list of 10 random integers in the range of 1 to 100 and
# print out the list
list = [randint(1, 100) for i in range(10)]
print("Sorting Process of a List of Integers by Bubble Sort:")
print(list)

# Use bubble sort to sort the integers in the list in ascending order
# with the updated list printed out after each swapping
for i in range(1, 10):
    noswapping = True
    for j in range(10 - i):
        if list[j] > list[j + 1]:
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
            print(list)
            noswapping = False
    if noswapping:
        break
