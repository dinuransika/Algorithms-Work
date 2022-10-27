pent=[]
i=0
for i in range(1,10000000):
    pe=i*(3*i-1)/2
    pent.append(pe)
mina=1000000000000000000
import random
for j in range(0,len(pent)*2):
    pi,pj=random.sample(pent,2)
    #Taking to values randomly.
    if abs(pi-pj) in pent and (pi+pj) in pent:
        if mina>abs(pi-pj):
            mina=abs(pi-pj)
            print mina

print mina
        
    
    
