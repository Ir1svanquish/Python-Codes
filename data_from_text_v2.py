# Manipulating the Data from a Text File
# Version 2

# Read the data of first marriages registered in HK from the file
with open('HKFM.txt', 'r') as infile:
    line = infile.readline() # Discard the title line
    line = infile.readline()
    year = line.strip('\n').split('\t')[1:]
    data = []
    sex = []
    for line in infile:
        if '\t' in line: # Check if the line has tab-delimited data
            row = []
            for i in line.strip('\n').split('\t'):
                row.append(i)
            data.append(row)
        else:
            sex.append(line)

def getdata(year, rawdata):
    """ Find the total number and dominant age group """
    nyr = len(year)
    total = [0 for i in range(nyr)]
    dag = ['' for i in range(nyr)]
    for i in range(nyr):
        max = 0
        for j in range(len(rawdata)):
            num = int(rawdata[j][i+1])
            if max < num:
                max = num
                dag[i] = rawdata[j][0]
            total[i] += num
    return total, dag

# Find the total number and dominant age group of first marriages
# by sex and year
nyr = len(year)
nag = int(len(data)/2) # Number of age groups
sex = ['Male', 'Female']
totalm, dagm = getdata(year, data[:nag])
totalf, dagf = getdata(year, data[nag:])

# Print a table of the results
print('{:>6s} {:>6s} {:>14s} {:>20s}'.format('Sex', 'Year', 'Total Number',\
'Dominant Age Group'))
print('-'*49)
for i in range(nyr):
    print('{:>6s} {:>6s} {:>14d} {:>20s}'.format(sex[0], year[i], totalm[i], dagm[i]))
for i in range(nyr):
    print('{:>6s} {:>6s} {:>14d} {:>20s}'.format(sex[1], year[i], totalf[i], dagf[i]))
