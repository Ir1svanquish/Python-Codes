# Opeations on a Line of text via string manipulation
# Written on: 23/03

string = str(input("Enter a line of text without punctuation mark:\n"))

print("Type a number 1 to 3 to do one of the following operations")
print(" 1 - print the line of text with all its blank spaces removed")
print(" 2 - print the line of text with each word in reversed order")
print(" 3 - print the number of words in the line of text")

num = int(input("Enter your choice (1-3): "))

if num == 1:
    print("The line of text with all its blank spaces removed:\n", string.replace(" ", ""))

elif num == 2:
    result = list()
    for i in range(len(string)):
        if strint[i] != " ":
            result.append(string[i])
        else:
            while len(result) > 0:
                print(result[-1], end = "")
                result.pop()
            print(end = " ")

    while len(result) > 0:
        print(result[-1], end = "")
        result.pop()

elif num == 3:
    words = string.split()
    count = 0
    for i in words:
        count += 1
    print("The number of words in the line of text:" , count)

else:
    print("Invalid input. You must type 1 or 2 or 3!")
