#!/usr/bin
from Eulerfunc import *
from time import time
start = time()
count = 0


def odd_digits(num):
    lis = str(num)
    suma = 0
    for i in lis:
        if int(i) % 2 != 0:
            suma += 1
    if suma == 0:
        return False
    elif suma == len(str(num)):
        return True


for i in range(1, 10**9):
    reverse_i = rev_num(i)
    if i % 10 == 0:
        continue
    if odd_digits(i + reverse_i):
        count += 1
        #print(i, reverse_i, i + reverse_i)
print(count)
print(time() - start)

