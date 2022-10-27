#!/usr/bin
from Eulerfunc import totient_func
from time import time
start = time()
count = 0
min_i = 0
min_r = 10**7
for i in range(1, 10**5):
    set_i = set(str(i))
    tot = totient_func(i)
    tot_set = set(str(tot))
    if set_i == tot_set and (i / tot) < min_r:
        min_i = i
print(min_i)
print(time() - start)
