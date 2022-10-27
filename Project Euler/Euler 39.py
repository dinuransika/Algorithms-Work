i=0
j=0
k=0
p=120
maxa=0
maxp=0
count=0
while p<1000:
    count=0
    p+=1
    i=0
    while i<p:
        i+=1
        j=0
        while j<p:
            j+=1
            k=0
            while k<p:
                k+=1
                if p==i+j+k and i*i==j**2+k**2:
                    count+=1
    if maxa<count:
        maxa=count
        maxp=p
        print maxp

print maxp
            
                    

                    
                    
        
