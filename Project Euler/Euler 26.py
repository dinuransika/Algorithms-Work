from time import time
start=time()
num=0
longest=0
def Prime(x):
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
for i in range(3,1000,2):
    if Prime(i)==True:
        primes.append(i)
for i in primes:
    if i==5:
        continue
    cou=1
    while (10**cou)%i!=1:
        cou+=1
    if cou>longest:
        num,longest=i,cou
print(num)
print(time()-start)
