#!/usr/bin
from Eulerfunc import *
from time import time
start = time()
primes = []
limit = 50000000
nums = set()
for i in range(1, int(limit**0.5)):
    if prime(i):
        primes.append(i)
for i in primes:
    for j in primes:
        if j > int(limit**(1/3)):
            continue
        for k in primes:
            if k > int(limit**0.25):
                continue
            if i**2 + j**3 + k**4 < limit:
                nums.add(i**2 + j**3 + k**4)
print(len(nums))
print(time() - start)
