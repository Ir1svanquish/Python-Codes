# Bubble Sort
# Written on: 23/03

import random

lst = list()
for i in range(10):
    lst.append(random.randint(1,100))
print(lst)

length = len(lst)

for j in range(length - 1):
    for k in range(0, length - j -1):
        if lst[k] > lst[k + 1]:
            lst[k], lst[k + 1] = lst[k + 1], lst[k]
            print(lst)
