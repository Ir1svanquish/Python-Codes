# Printing a Histogram
# Version 1

data = {"Centrial & Western" : 7, "Wan Chai" : 25, "Eastern" : 22, "Southern" : 8, \
        "Yau Tsim Mong" : 14, "Sham Shui Po" : 22, "Kowloon City" : 29, "Wong Tai Sin" : 6,\
        "Kwun Tong" : 15, "Sai Kung" : 7, "Sha Tin" : 8, "Tai Po" : 8,\
        "North" : 8, "Yuen Long" : 27, "Tsuen Mun" : 7, "Tsuen Wan" : 18,\
        "Kwai Tsing" : 0, "Islands": 0}

print("Accommodation in Government Primary Schools by Districts in HK, 2019")
print("(in nearest hundreds)")

for i in data:
    asterisk = ""
    for j in range(data[i]):
        asterisk += "*"
    print("{0:>18} | {1} ({2})".format(i, asterisk, data[i]))
