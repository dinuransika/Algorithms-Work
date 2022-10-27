i=1
j=1
com=[]
while i<100:
    i+=1
    j=1
    while j<100:
        j+=1
        e=i**j
        if e not in com:
            com.append(e)
            
            

print(len(com))
    
    
