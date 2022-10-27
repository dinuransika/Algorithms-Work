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


i=0
primes=[]
while i<1000000:
    i+=1
    if prime(i)==True:
        primes.append(i)

#print(len(primes))
n=0
m=550
maxa1=0
maxa=0
while n<(len(primes)):
    su=0
    ch=0
    for j in range(0,n):
        ch+=1
        su+=primes[j]
        if prime(su)==True:
            if ch>maxa:
                maxa1=su
                maxa=su
    n+=1
    print maxa

print maxa
    
    
    
