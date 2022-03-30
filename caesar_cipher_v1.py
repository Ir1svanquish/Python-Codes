# Caesar Cipher
# Version 1

string = str(input("Enter a plain text to be encrypted:\n"))
key = int(input("Enter a key in range [1, 25]:\n"))
result = list()

if key >= 1 and key <= 25:
    for i in range(len(string)):
        char = string[i]
        if string[i] == " ":
            result.append(char)
        elif (char.isupper()):
            result.append(chr((ord(char) + key - 65) % 26 + 65))
        else:
            result.append(chr((ord(char) + key - 97) % 26 + 97))
    print("The cipher text is:")
    for j in result:
        print(j, end = "")

    key2 = int(input("\nEnter the key again:\n"))
    print("The decrypted cipher text is:")
    for k in result:
        if (k.isupper()):
            k = chr((ord(k) - key2 - 65) % 26 + 65)
        elif (k.islower()):
            k = chr((ord(k) - key2 - 97) % 26 + 97)
        print(k, end = "")

else:
    print("Invalid key!")
