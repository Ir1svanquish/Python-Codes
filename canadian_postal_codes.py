# Exercise 1
# Canadian Postal Codes
# Name: Chan kit Chi UID: 3035779167 Written on: 06/04

code = input("Enter a Canadian postal code: ")
code = code.replace(" ", "")

area_dict = {"A":"Newfoundland and Labrado", "B":"Nova Scotia", "C":"Prince Edward Island", "E":"New Brunswick", "G":"Quebec", "H":"Quebec",\
        "J":"Quebec","K":"Ontario", "L":"Ontario", "M":"Ontario", "N":"Ontario", "P":"Ontario", "R":"Manitoba", "S":"Saskatchewan",\
        "T":"Alberta", "V":"British Columbia", "X":"Nunavut or Northwest Territories", "Y":"Yukon"}

area = code[0]
region = code[1]

if area in area_dict:
    if region == '0':
        print(f"The postal code is for a rural address in {area_dict[area]}.")
    elif (ord(region) > 48 and ord(region) <= 57):
        print(f"The postal code is for a urban address in {area_dict[area]}.")
    else:
        print("The second character in the postal code must be a digit!")
else:
    print("The first character in the postal code is invalid!\nIt cannot be D, F, I, O, Q, U, W, or Z!")
    
