# Recursive Function to evaluate a finite sum
# Version 2

def fsum(x, n):
    """ Compute the finite sum for x/(1-x)^2 with a recursive app """
    if n == 1:
        return x
    return n * x ** n + fsum(x, n - 1)

x_list = [0.1, 0.2, 0.3, 0.4]
n_list = [2, 5, 10, 50, 100]

# Display the results for calling the function with different values
# of x and n
for x in [0.1, 0.2, 0.3, 0.4]:
    print('x = ', x)
    for n in [2, 5, 10, 50, 100]:
        print('n = {:d}, sum = {:.8f}'.format(n, fsum(x, n)))
