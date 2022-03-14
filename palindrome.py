# palindrome.py
# This program determines whether a five-digit integer is a palindrome.

while True:
    n = int(input("Enter a five-digit number: "))
    if (n >= 10000) and (n < 100000):
        break
    print("Invalid input!")

d1 = n % 10
d2 = (n % 100) // 10
d4 = (n % 10000) // 1000
d5 = (n % 100000) // 10000
if ((d1 == d5) and (d2 == d4)):
    print(n, "is a palindrome.")
else:
    print(n, "is not a palindrome.")
