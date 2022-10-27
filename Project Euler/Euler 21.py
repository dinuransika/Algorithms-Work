i=0
su2=0
while i<10000:
    i+=1
    j=0
    su=0
    while j<(i-1):
        j+=1
        if i%j==0:
            su+=j
    if su!=i:
        j=0
        su1=0
        while j<(su-1):
            j+=1
            if su%j==0:
                su1+=j
        if i==su1:
            su2+=i

print(su2)
            
       
            
                
    
