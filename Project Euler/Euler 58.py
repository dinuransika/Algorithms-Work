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
square=[]
while n<100000:
    n+=1
    square.append(n**2)


n=1
m=0
t=0

while n<26:
    ni=int(n)
    if prime(ni)==True:
        t+=1
    if (ni-1) in square and not(ni==1):
        print (t/(ni-1)**0.5)*100,'%'
    n+=0.5
    
   
    
