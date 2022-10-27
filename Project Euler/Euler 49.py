from Eulerfunc import *
from itertools import permutations
for cou in range(1000,10000):
    a = cou
    if prime(a):
        perm = permutations(list(str(a)),4)
        c=0
        li=[]
        for i in perm:
            p=3
            suma=0
            for j in i:
                suma+=int(j)*10**p
                p-=1
            if prime(suma):
                li.append(suma)
        li.sort()
        li.remove(cou)
        li.insert(0,cou)
        for i in li:
            if cou-i!=0 and 2*i-cou in li and len(li)!=2:
                print(cou,2*i-cou)
                break
            
