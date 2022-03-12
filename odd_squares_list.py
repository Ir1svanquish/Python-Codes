# odd_squares_list.py
# This program accepts a sequence of comma-separated integers and uses
# list comprehension to generate a list of the squares of each odd
# integer in the sequence.

instr = input("Enter a sequence of comma-separated integers: ")
ele = instr.split(",")
lst = []
for ch in ele:
    lst.append(int(ch))

oddsq = [i*i for i in lst if i % 2 == 1]
print("Squares of the odd numbers in the sequence:", end = "")
for i in range(len(oddsq) - 1):
    print(oddsq[i], end = ",")

print(oddsq[-1])
