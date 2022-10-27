x=100
y=1001
pal=[]
import math
while y>100:
   y-=1
   x=100
   while x<1000:
        d=x*y
        dc=d
        e=len(str(d))
        su1=0
        while 0<e:
            e-=1
            rem=dc%10
            dc/=10
            su1+=rem*(math.pow(10,e))
        if d==su1:
            pal.append(d)
        x+=1


print(max(pal))

 
    
    
