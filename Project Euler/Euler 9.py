i=0
j=0
k=0

while i<1000:
    i+=1
    j=0
    while j<1000:
        j+=1
        k=0
        while k<1000:
            k+=1
            if i+j+k==1000:
                if i*i+j*j==k*k:
                    print(i)
                    print(j)
                    print(k)
