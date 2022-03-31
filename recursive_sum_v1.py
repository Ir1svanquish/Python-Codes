# Recursive Function to evaluate a finite sum
# Version 1

def fsum(x,n):
    if n == 1:
        return x
    else:
        return n * x ** n + fsum(x, n - 1)

x_list = [0.1, 0.2, 0.3, 0.4]
n_list = [2, 5, 10, 50, 100]

for x in x_list:
    for n in n_list:
        print(f'The value of sum for x = {x} and n = {n}')
        print(format(fsum(x, n), '.8f'))
