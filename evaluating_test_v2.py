# Evaluating a Test with Arrays
# Version 2

# Import the numpy module
import numpy as np

# Read the string of the correct answers to the questions from the
# user and store the answers into an array of characters
ans_str = input('Enter the correct answers to the MC questions:\n')
ans = np.array([ch for ch in ans_str])

# For each student, read the string of the student's answers from the
# user and store the answers into an array of characters, construct a
# Boolean array to indicate whether the answer of the student to each
# question is correct, use this array to count the number of correct
# answers and print the results
for i in range(1, 6):
    stdans_str = input('\nEnter the answers of Student-' + str(i) + ':\n')
    stdans = np.array([ch for ch in stdans_str])
    correct = (ans == stdans)
    ncans = np.sum(correct)
    print('Number of correct answers:', ncans)
    if ncans == ans.size:
        print('Answers to the following questions are correct: ALL')
    elif ncans > 0:
        print('Answers to the following questions are correct: ')
        for j in range(ans.size):
            if correct[j]:
                print(j + 1, end = ' ')
        print()
