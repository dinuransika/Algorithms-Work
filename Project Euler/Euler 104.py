#!/usr/bin
from time import time
from math import log10, pow
start = time()
def top_digits(n):
    phi = (1 + 5**0.5) / 2
    t = n*log10(phi) + log10(1 / 5**0.5)
    t = int(pow(10, t - int(t) + 8))
    return t
pan1_9 = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
n1 = 1
n2 = 1
i = 2
while True:
    i += 1
    fibo = (n1 + n2)%10**9
    n1 = n2
    n2 = fibo
    top = top_digits(i)
    if (set(list(str(fibo))) == pan1_9) and (set(list(str(top))) == pan1_9):
        print(i)
        break
print(time() - start)  
