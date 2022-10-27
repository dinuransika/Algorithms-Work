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
x=0
n=1
while n<100000:
    n+=2
    if prime(n)==False:
        t=0
        while t<n:
            t+=1
            if prime(t)==True:
                x=0
                sqt=int(n**0.5)
                for i in range(1,sqt+1):
                    su=t+2*i**2
                if su==n:
                    x+=1
                    if x==0:
                        print n
                    
            
                
