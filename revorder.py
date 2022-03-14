# revorder.py
# This program prints a long string with the words in reverse order.

lstr = input("Enter a long string: ")

lstrsp = " ".join(lstr.split(" ")[::-1])
print("The string with word order reversed: ", lstrsp)
