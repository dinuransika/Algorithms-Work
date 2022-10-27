tot=0
for ic in range(1,10000000):
    i=ic
    while True:
        suma=0
        p=len(str(i))
        while p!=0:
            suma+=(i%10)**2
            p-=1
            i//=10
        i=suma
        if suma==89:
            tot+=1
            break
        if suma==1:
            break
print(tot)
