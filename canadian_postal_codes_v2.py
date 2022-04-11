# Canadian Postal Codes
# Version 2

# Construct a dictionary for the first characters in the postal code
# to the province or territory
district = {'A':'Newfoundland and Labrador', 'B':'Nova Scotia',
'C':'Prince Edward Island', 'E':'New Brunswick',
'G':'Quebec', 'H':'Quebec', 'J':'Quebec', 'K':'Ontario',
'L':'Ontario', 'M':'Ontario', 'N':'Ontario',
'P':'Ontario', 'R':'Manitoba', 'S':'Saskatchewan',
'T':'Alberta', 'V':'British Columbia',
'X':'Nunavut or Northwest Territories', 'Y':'Yukon'}
# Read a Canadian postal code from the user
pcode = input('Enter a Canadian Postal Code: ')
# Display whether the postal code refers to an urban or a rural
# address along with the associated province or territory
ch1 = pcode[0]
if not (ch1 in district):
    print('The first character in the postal code is invalid!')
    print('It cannot be D, F, I, O, Q, U, W, or Z!')
else:
    ch2 = pcode[1]
if (ord(ch2) < 48) or (ord(ch2) > 57):
    print('The second character in the postal code must be a digit!')
else:
    print('The postal code is', end=' ')
if ord(ch2) == 48:
    print('a rural address in', end=' ')
else:
    print('an urban address in', end=' ')
    print('{:s}.'.format(district[ch1]))
