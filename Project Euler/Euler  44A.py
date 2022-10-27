pent=[]
for i in range(1,1000000):
    pe=i*(3*i-1)/2
    pent.append(pe)
mina=1000000000000000000
for pi in pent:
    for pj in pent:
        if abs(pi-pj) in pent and (pi+pj) in pent:
            if mina>abs(pi-pj):
                mina=abs(pi-pj)
                print mina

print mina
        
    
