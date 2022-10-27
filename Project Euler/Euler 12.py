from time import time
start=time()
x=100000000
tri=0
while x<1500000000:
    x+=1
    tri=(x*(x+1))/2
    t=0
    k=0
    while t<tri+1:
        t+=1
        if tri%t==0:
            k+=1
    if k>500:
        print("\n")
        print(tri)
print(time()-start)
    
   
            
    
    
    
