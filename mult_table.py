# mult_table.py
# This program prints the multiplication table showing all multiples
# from 1xn to nxn where 0 < n <= 10 using the for statement.

n = int(input("Please input a positive integer n that 0 < n <= 10: "))
available = 1

if n <= 0 or n > 10:
    print("Invaild input!")
    available = 0

if available == 1:
  for i in range(1, n+1):
      print(i, "x", n, "=", i * n)
