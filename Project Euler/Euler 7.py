def prime(x):
    i=0
    t=0
    while i<x:
        i+=1
        if x%i==0:
            t+=1
    if t==2:
        return True
    else:
        return False



k=0
j=0
while k<10001:
    j+=1
    if prime(j)==True:
        k+=1
print(j)
    
    
            
    
