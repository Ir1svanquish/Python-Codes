"""

Encrypt number

"""
mydict = {'0' : 'Z', '1' : 'X', '2' : 'T', '3' : 'J', '4' : 'A', '5' : 'W', '6' : 'F', '7' : 'S', '8' : 'B', '9' : 'V'}
old_string = str(input())
result = ''
for x in old_string:
    result += mydict[x]
print(result)
