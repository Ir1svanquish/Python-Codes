# divisors.py
# This program prints a list of all the divisors of an integer.

n = int(input("Enter an integer: "))

print("This number has divisors: ")
for i in range(1, n+1):
    if (n % i) == 0:
        print(i)
