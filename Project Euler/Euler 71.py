#!/usr/bin
from time import time
start = time()
N = 3 / 7
max_div = 0
min_nu = 0
for i in range(10**6, 10**6 - 100, -1):
    for j in range(1, int(N * i) + 1):
        if (j / i) < N and  (j / i) > max_div:
            max_div = (j / i)
            min_nu = j
            #print(j, i)
print(max_div, min_nu)
print(time() - start)
