# effective_of_model.py
# This program produce the precentage error of a model
# constructed by having N (N is an even number) particles of charge Q/N 
# at the appropriate locations to illustrate how effective this model is.

import math

true = 7.90
q = 1.6e-9
x = 2
k_0 = 9e9
error = []

for i in range(2, 18, 2):
    sum = 0
    diff = 1 / i
    seq = 2 / i
    half = int(i / 2)
    before = 2 - diff
    sum += ((q / i) / (before))
    after = 2 + diff
    sum += ((q / i) / (after))
    for j in range(half):
        if j != 0:
            sum += ((q / i) / (before - j * seq))
            sum += ((q / i) / (after + j * seq))
    calc = k_0 * sum
    error.append((calc - true) / true)

m = 0
for n in range(2, 18, 2):
    percentage = error[m] * 100
    print(f"The percentage error of the model constructed by having {n} particles of \
Q/N at the appropriate locations is {percentage}%.")
    m += 1
