#!/usr/bin
from Eulerfunc import *
from time import time
start = time()
a_count = 0
for i in range(2, 10**6, 2):
    factor = factors(i)
    count = 0
    for j in factor:
        if prime(j + i / j):
            count += 1
        else:
            break
    if count == len(factor):
        a_count += 1
print(a_count)
print(time() - start)
