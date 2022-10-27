n=0
while n<100000:
    n+=1
    tri=n*(n+1)/2
    m=0
    while m<100000:
        m+=1
        if m*(3*m-1)/2==tri:
            p=0
            while p<100000:
                p+=1
                if p*(2*p-1)==tri:
                    print tri
            
    
    
