# Evaluating a Test with Arrays
# Version 1

answer_0 = input("Enter the correct answers to the MC questions:\n")
array_0 = list(answer_0)

for i in range(1, 6):
    answer_1 = input(f"Enter the answers of Student-{i}:\n")
    array_1 = list(answer_1)
    correct = 0
    position = []
    for j in range(len(array_0)):
        if array_0[j] == array_1[j]:
            correct += 1
            position.append(j + 1)
    print("Number of correct answers:", correct)
    print("Answers to the following questions are correct:")
    if correct == len(array_0):
        print("ALL\n")
    else:
        for k in range(len(position)):
            print (position[k], end = " ")
        print("\n")
