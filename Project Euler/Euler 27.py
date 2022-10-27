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
   
   
n=0
a=-1000
b=-1000
t=0
maxa=0
ac=0
bc=0
while a<1000:
    a+=1
    b=-1000
    while b<1000:
        b+=1
        n=-1
        t=0
        k=0
        while t!=1:
            n+=1
            z=n*n+a*n+b
            if prime(z)==False:
                t+=1
            k+=1
        if maxa<k:
            maxa=k
            ac=a
            bc=b

print(ac*bc)
        
            
            
        
