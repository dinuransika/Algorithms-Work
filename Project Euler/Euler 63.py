a=0
k=0
while a<100:
    a+=1
    b=100
    while b>0:
        b-=1
        e=a**b
        y=len(str(e))
        if b==y:
            k+=1

print(k)
            
    
