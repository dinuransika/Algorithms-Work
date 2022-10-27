i=0
import math
while i<20000000:
    i+=1
    ic=i
    su=0
    while ic!=0:
        rema=ic%10
        ic/=10
        su+=math.factorial(rema)
    if i==su:
        print(i)
    
        
