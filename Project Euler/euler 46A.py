#!/usr/bin
#created by Dii
from time import time
start=time()
def prime(x):
    if x<2:
        return False
    elif x==2 or x==3:
        return True
    else:
        i=1
        while i<int(x**0.5+1):
            i+=1
            if x%i==0:
                return False
                break
            else :
                continue
        else:
            return True
primes=[]
for i in range(2,10000):
    if prime(i)==True:
        primes.append(i)
odds=[]
for i in range(3,10000,2):
    odds.append(i)
comp=list(set(odds)-set(primes))
ans=[]
for i in comp:
    cou=0
    for j in primes:
        if j<i:
            for k in range(1,int(i**0.5)):
                co=j+2*k**2
                if co==i:
                    cou+=1
                    break
        else:
            break
    if cou==0:
        ans.append(i)
        break
    if len(ans)!=0:
        break

print(min(ans))
print(time()-start)        
