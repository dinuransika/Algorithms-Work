def abundant(x):
    fac=[]
    a=0
    while a<x-1:
        a+=1
        if x%a==0:
            fac.append(a)
    if sum(fac)>x:
        return True
    else:
        return False
a=0
inti=[]
while a<28123:
    a+=1
    inti.append(a)
a=0
ab=[]
inti=set(inti)
while a<28123:
    a+=1
    if abundant(a)==True:
        ab.append(a)
from itertools import combinations
for i in list(ab):
    f=i+i
    inti.discard(i+i)
comb=combinations(ab,2)
for i in list(comb):
    inti.discard(sum(i))
inti=list(inti)
print(sum(inti))
