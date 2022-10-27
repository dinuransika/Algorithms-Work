num1=0
import math
while num1 < 200:
    num1+=1
    sum1=0
    numc=num1
    while num1>0:
        rema=num1%10
        sum1+=(math.pow(rema,3))
        num1=num1/10
    if sum1==numc:
        print(numc)
