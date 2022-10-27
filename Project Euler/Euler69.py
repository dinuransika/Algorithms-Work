from Eulerfunc import *
from time import time
start=time()
maxtotient=0
primes=[]
nu=1
for i in range(1,10000):
    if prime(i)==True:
        primes.append(i)
for i in primes:
    if nu*i>1000000:
        break
    nu*=i

print(nu,nu/totient_func(nu),totient_func(nu))
print(time()-start)
