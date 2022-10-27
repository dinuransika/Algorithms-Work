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


i=10
while i<20:
    i+=1
    t=0
    k=0
    ic=i
    while ic!=1:
        t+=1
        if ic%t==0:
            if prime(t)==True:
                k+=1
            tc=t
            t=0
        ic/=tc
if k==2:
    print i
            
