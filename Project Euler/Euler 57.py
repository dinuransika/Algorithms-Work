#!/usr/bin
from fractions import Fraction
from time import time
start = time()
count = 0
init = Fraction(3, 2)
for i in range(1, 1000):
    init = 1 + (1 / (init + 1))
    if len(str(init.numerator)) > len(str(init.denominator)):
        count += 1
print(count)
print(time() - start)
