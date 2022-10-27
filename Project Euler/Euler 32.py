#!/usr/bin
#created by dii
from time import time
start=time()
se=set('123456789')
suma=set()
for i in range(1,9):
    for j in range(999,4999):
        k=i*j
        si=str(i)
        sj=str(j)
        sk=str(k)
        stot=si+sj+sk
        if len(stot)==9 and set(stot)==se:
            suma.add(k)
        elif len(stot)>9:break
for i in range(9,99):
    for j in range(99,999):
        k=i*j
        si=str(i)
        sj=str(j)
        sk=str(k)
        stot=si+sj+sk
        if len(stot)==9 and set(stot)==se:
            suma.add(k)
        elif len(stot)>9:break
print('Answer =',sum(suma))
print('Elapsed time =',time()-start)
