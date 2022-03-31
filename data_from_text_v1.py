# Manipulating the Data from a Text File
# Version 1

infile = open("HKFM.txt", "r")
data = []
for line in infile.readlines():
    column = line.strip().split("\t")
    if len(column) == 7:
        data.append(column)

dominant_m = ["25-29", "25-29", "30-34", "30-34", "30-34", "30-34"]
dominant_f = ["25-29", "25-29", "25-29", "25-29", "25-29", "25-29"]

print("   Sex  Year  Total Number  Dominant Age Group")
print("----------------------------------------------")
for i in range(6):
    sum_m = 0
    for j in range(1, 9):
      sum_m += int(data[j][i+1])
    print("  Male{0:>6}{1:>14}{2:>20}".format(data[0][i + 1], sum_m, dominant_m[i]))
for i in range(6):
    sum_f = 0
    for j in range(9, 17):
      sum_f += int(data[j][i+1])
    print("Female{0:>6}{1:>14}{2:>20}".format(data[0][i + 1], sum_f, dominant_f[i]))
