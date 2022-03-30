# Caesar Cipher
# Version 2

# Input a key value and a plain text. Ask the user to input again if
# the input key value is invalid

while True:
    n = int(input('Enter a key value n (1-25): '))
    if n > 0 and n < 26:
        break
    print('Invalid input! n must be an integer in the range of 1-25!')
string = str(input('Enter a plain text: '))

# Construct the strings for the plain text and cipher text letters
plaintxtlett = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertxtlett = plaintxtlett[n: 26]
ciphertxtlett += plaintxtlett[0: n]
ciphertxtlett += plaintxtlett[n + 26: 52]
ciphertxtlett += plaintxtlett[26: n + 26]

# Encode the plain text and output the result
cipher_text = ''
for ch in string:
    if ch != ' ':
        index = plaintxtlett.index(ch)
        cipher_text += ciphertxtlett[index]
    else:
        cipher_text += ' '
print('The cipher text is', cipher_text)

# Decode the plain text and output the result
decryp_text=''
for ch in cipher_text:
    if ch != ' ':
        index = ciphertxtlett.index(ch)
        decryp_text += plaintxtlett[index]
    else:
        decryp_text += ' '
print('The decrypted cipher text is', decryp_text)
