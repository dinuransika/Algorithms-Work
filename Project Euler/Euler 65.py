#!/usr/bin
from fractions import Fraction
from time import time
start = time()
init = Fraction(2, 1)
for i in range(1, 10):
    if i % 2 == 1:
        init = 1 + (1 / (init + 1))
    
print(time() - start)
