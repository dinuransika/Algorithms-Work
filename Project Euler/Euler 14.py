j=0
maxa=0
while j<1000000:
    j+=1
    i=j
    k=1
    while i!=1:
        k+=1
        if i%2==0:
            i/=2
        else:
            i=3*i+1
    if maxa<k:
        maxa=k
        c=j

print(c,maxa)


        
