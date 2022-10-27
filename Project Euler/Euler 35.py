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
j=0
t=0

while j<1000:
    j+=1
    e=len(str(j))
    ec=e
    if prime(j)==True:
        i=j
        ic=i
        k=0
        e-=1
        ec-=1
        while ec!=0:
            ec-=1
            rema=i%(10**e)
            i=i//(10**e)
            i=i+(rema*10)
            if prime(i)==True:
                k+=1
        if k==e:
            t+=1

print(t)
            
