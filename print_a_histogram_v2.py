# Printing a Histogram
# Version 2

# Define two lists to store the district names and the number of
# students in each district
district = ['Central & Western', 'Wan Chai', 'Eastern', 'Southern', \
'Yau Tsim Mong', 'Sham Shui Po', ' Kowloon City', \
'Wong Tai Sin', 'Kwun Tong', 'Sai Kung', 'Sha Tin', \
'Tai Po', ' North', 'Yuen Long', 'Tuen Mun', 'Tsuen Wan', \
'Kwai Tsing', 'Island']
studentnum = [7, 25, 22, 8, 14, 22, 29, 6, 15, 7, 8, 8, 8, 27, 7, 18, 0, 0]

# Print a histogram to show the statistics of the given data
print('Accommodation in Government Primary Schools by Districts in \
HK, 2019')
print('(in nearest hundreds)')
for i in range(len(district)):
    print('{:>17s} | '.format(district[i]), end='')
    if studentnum[i] != 0:
        print('{:s} ({:d})'.format('*'*studentnum[i], studentnum[i]))
    else:
        print('(0)')
