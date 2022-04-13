# carbon13.py
# This program uses the numpy.random function binomial to estimate
# the abundances of C60 with exactly zero, one, two, three and four
# carbon-13 (13C) atoms and compare them with the exact answers.

import numpy as np
n, x, mmax = 60, 0.0107, 4
m = np.arange(mmax + 1)
# Estimate the abundances by random sampling from the binomial
# distribution
ntrials = 10000
pbin = np.empty(mmax + 1)
data = np.random.binomial(n, x, ntrials)
for r in m:
    pbin[r] = np.sum(data == r)/ntrials
    
# Calculate the exact answers from binomial distribution nCm
nCm = np.empty(mmax+1)
nCm[0] = 1
for r in m[1:]:
    nCm[r] = nCm[r - 1]*(n - r + 1) / r
p = nCm * (x ** m)*(1 - x)**(n - m)
# Display the results
print("Abundances of C60 as (13C)[m]")
print("{:1s} {:>7s} {:>10s}".format("m", "Exact", "Estimated"))
print("-"*20)
for r in m:
    print("{:1d} {:7.4f} {:10.4f}".format(r, p[r], pbin[r]))
