# charcount.py
# This program counts and prints the numbers of each character in a
# string input by console.

instr = input("Enter a string: ")
charcount = {}
for ch in instr:
    if charcount.get(ch) == None:
        charcount[ch] = 1
    else:
        charcount[ch] += 1

print("Numbers of each character in this string:")
print("{:>9s} {:>8s}".format("Character", "Numbers"))
print("{:18s}".format("-" * 18))
for ch, chcount in sorted(charcount.items()):
    print("{:^9s} {:^7d}".format(ch, chcount))
