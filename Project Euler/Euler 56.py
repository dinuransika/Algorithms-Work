a=0
b=100
digit_sum=[]
while a<100:
    a+=1
    b=100
    while b>0:
        b-=1
        e=a**b
        ec=e
        su=0
        while ec!=0:
            rema=ec%10
            su+=rema
            ec//=10
        digit_sum.append(su)
    
print(max(digit_sum))
            
        
