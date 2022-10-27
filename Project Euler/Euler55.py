from Eulerfunc import *
from time import time
start=time()
lyrical=[]
for j in range(1,10000):
    cou=0
    i=j
    while True:
        if palindromic(i+rev_num(i))==True:
            break
        else:
            i=(i+rev_num(i))
        if cou==50:
            lyrical.append(j)
            break
        cou+=1
print(len(lyrical))
print(time()-start)
