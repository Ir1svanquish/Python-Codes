# sum_of_cubes.py
# This program prints the sum of the cubes of all the positive integers
# smaller than an input number using a while statement.

n = int(input("Please input a positive integer: "))
sum = 0
available = 1

if n <= 0:
    print("Invaild input!")
    available = 0

for i in range(n + 1):
    sum += i ** 3

if available == 1:
  print("The sum of the cubes of all the positive integers", end=" ")
  print("up to", n, "is", sum)
