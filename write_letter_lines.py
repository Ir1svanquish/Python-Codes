# write_letter_lines.py
# This program creates a file in which all letters in the English
# alphabet are listed in order by specified number of letters on
# each line.

while True:
    n = int(input("Enter the number of letters per line: "))
    if (n > 0) and (n <= 26):
        break

alphabet = ""
for i in range(26):
    alphabet += chr(i+65)

with open("letterlines.txt", "w") as outfile:
    letters = [alphabet[i:i+n] + "\n" for i in range(0, len(alphabet), n)]

for line in letters:
    outfile.write(line)
