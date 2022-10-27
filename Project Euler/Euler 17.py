_1_9=['0','3','3','5','4','4','3','5','5','4']
_10_19=['3','6','6','8','8','7','7','9','8','8']
_20_99=['0','6','6','5','5','5','7','6','6']

n=0
sumn=0
while n<999:
    n+=1
    len1=len(str(n))
    if len1==1:
        sumn+=int(_1_9[n])
    elif len1==2:
        if n<20:
            sumn+=int(_10_19[n%10])
        else: 
            po10_0=n%10
            po10_1=n//10
            sumn+=int(_1_9[po10_0])
            sumn+=int(_20_99[(po10_1)-1])
    else:
        twodig=n%100
        po10_2=n//100
        sumn+=(int(_1_9[po10_2])+10)
        if twodig<10:
            po10_0=twodig%10
            sumn+=int(_1_9[po10_0])
        elif twodig<20:
            sumn+=int(_10_19[twodig%10])
        else:
            po10_0=twodig%10
            po10_1=twodig//10
            sumn+=int(_1_9[po10_0])
            sumn+=int(_20_99[po10_1-1])

print sumn+11-27
    
            
            
        
        
        
        
        

