#!/usr/bin
from time import time
start = time()
fraction_set = set()
fraction_count = 0
for i in range(1, 12001):
    for j in range(1, i - 1):
        if 1 / 3 < j / i < 0.5:
            fraction_set.add(j/i)
print(len(fraction_set))
print(time() - start)
