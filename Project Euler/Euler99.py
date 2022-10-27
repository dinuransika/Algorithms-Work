#!/usr/bin
# Euler 99
from time import time
from math import log
start = time()
fo = open("p099_base_exp.txt", "r")
maxexp = [519432, 525806]
counter_max = 0
counter = 0
for lines in fo.readlines():
    counter += 1
    li = lines.split(",")
    if int(li[1]) * log(int(li[0])) - maxexp[1] * log(maxexp[0]) > 0:
        maxexp, counter_max = [int(li[0]), int(li[1])], counter
print(maxexp, counter_max)
print(time()-start)
fo.close()
