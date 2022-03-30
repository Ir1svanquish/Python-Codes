# Exercise 3
# Printing a Histogram to a Text File

infile = open("HKPop2020data.txt", "r")
data = []
for line in infile.readlines():
    column = line.strip().split()
    if len(column) == 3:
        data.append(column)

for i in range(len(data)):
    for j in range(1, 3):
        data[i][j] = round(int(data[i][j]), -4) // 10000

print("Mid-year Population in Hong Kong by Age Group and Sex for 2020")
print("(in nearest ten thousands)")
for i in range(len(data)):
    symbol = ""
    for j in range(data[i][1]):
        symbol += "#"
    for j in range(data[i][2]):
        symbol += "%"
    print("{0:>5} | {1} ({2}/{3})".format(data[i][0], symbol, data[i][1], data[i][2]))
print("#-Male; %-Female")
