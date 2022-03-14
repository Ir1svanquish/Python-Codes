# strlower.py
# This program prints a string in lower case without using the
# string.lower method.

s = input("Enter a string: ")
sl = ""
for ch in s:
    if (ord(ch) >= 65) and (ord(ch) <= 90):
        sl += chr(ord(ch)+32)
    else:
        sl += ch
print(sl)
