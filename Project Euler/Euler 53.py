import math

n=0
con=0
while n<100:
    n+=1
    r=0
    while r<n:
        r+=1
        ncr=math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
        if ncr>1000000:
            con+=1

print con
