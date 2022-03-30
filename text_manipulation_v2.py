# Opeations on a Line of text via string manipulation
# Version 2

# Input a line of text without punctuation mark
string = input('Enter a line of text without punctuation mark:\n')
# Ask the user to choose the operation to be done on the line of text
# and perform the chosen operation only if the user choice is valid
print('Type a number 1 to 3 to do one of the following operations')
print(' 1 - print the line of text with all its blank spaces removed')
print(' 2 - print the line of text with each word in reversed order')
print(' 3 - print the number of words in the line of text')
choice = int(input('Enter your choice (1-3): '))

if choice == 1:
    output = 'The line of text with all its blank spaces removed:\n'
    output += "".join(string.split(" "))
elif choice == 2:
    output = 'The line of text with each word in reversed order:\n'
    stringsp = string.split(" ")
    output += stringsp[0][::-1]
    for words in stringsp[1:]:
        output += ' '
        output += words[::-1]
elif choice == 3:
    output = 'The number of words in the line of text: '
    stringsp = string.split(" ")
    count = 0
    for words in stringsp:
        if words != '':
            count += 1
    output += str(count)
else:
    output = 'Invalid input. You must type 1 or 2 or 3!'
# Output the result of the operation if the user choice of operation is
# valid; otherwise output an error message
print(output)
