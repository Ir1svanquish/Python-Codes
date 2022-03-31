# Printing a Histogram to a Text file
# Version 2

# Read the data of the 2020 mid-year population in HK from the file
with open('HKPop2020data.txt', 'r') as infile:
    line = infile.readline() # Discard the title line
    line = infile.readline() # Discard the header line
    data = []
    for line in infile:
        row = []
        for i in line.strip('\n').split(' '):
            row.append(i)
        data.append(row)

# Extract the statistics from the data and show them by printing a
# histogram to another file
with open('HKPop2020hist.txt', 'w') as outfile:
    print('Mid-year Population in Hong Kong by Age Group and Sex for '\
    +'2020', file = outfile)
    print('(in nearest ten thousands)', file = outfile)
    for i in range(len(data)):
        num_m = int(round(int(data[i][1]) / 10000))
        num_f = int(round(int(data[i][2]) / 10000))
        print('{:>5s} |'.format(data[i][0]), end = ' ', file = outfile)
        print('{:s}{:s}'.format('#' * num_m, '&' * num_f), end = ' ', file = outfile)
        print('({:d}/{:d})'.format(num_m, num_f), file = outfile)
    print('#-Male; &-Female', file = outfile)
