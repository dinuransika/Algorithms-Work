#!/usr/bin
from time import time
start=time()
from itertools import permutations
perm=list(permutations(['1','2','3','4','5','6','7','8','9'],9))
for i in range(9,10000):
    a=1
    suma=str(i)
    while True:
        a+=1
        suma+=str(a*i)
        if len(suma)>=9:
            break
    puma=tuple(suma)
    if puma in perm:
        print(suma)
print(time()-start)
