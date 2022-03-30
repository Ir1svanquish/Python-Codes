# Vector Manipulation
# Version 1

string_1 = input("Enter the vector A: ")
string_2 = input("Enter the vector B: ")

vector_1 = string_1.strip("[]").split(",")
vector_2 = string_2.strip("[]").split(",")


len_1 = len(vector_1)
len_2 = len(vector_2)

if len_1 != len_2:
    print("Invalid input! Vectors A and B must have the same length.")

else:
    result_1 = list()
    result_2 = list()
    result_3 = 0
    for i in range(len_1):
        result_1.append(int(vector_1[i]) + int(vector_2[i]))
        result_2.append(int(vector_1[i]) - int(vector_2[i]))
        result_3 += int(vector_1[i]) * int(vector_2[i])

    print("A+B = ", result_1)
    print("A-B = ", result_2)
    print("A.B = ", result_3)
