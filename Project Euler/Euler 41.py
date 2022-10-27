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

i=100000000
while i<1000000000:
    i+=1
    if prime(i)==True:
        istr=str(i)
        le=len(istr)
        t=0
        k=0
        while k!=le:
            k+=1
            if str(k) in istr:
                t+=1
        if t==le:
            print(i)
        


