def same_digits(x):
    digits=[]
    lenght=len(str(x))
    xc=x
    while lenght!=0:
        rema=xc%10
        xc//=10
        lenght-=1
        digits.append(rema)
    a=('2','3','4','5','6')
    t=0
    for i in a:
        mult=int(i)*x
        lenght=len(str(mult))
        le=lenght
        xc=mult
        while lenght!=0:
            rema=xc%10
            xc//=10
            lenght-=1
            if rema in digits:
                t+=1
    if t==(le*5):
        return True
    else:
        return False

n=1
while n!=0:
    if same_digits(n)==True:
        print n
    n+=1
    
            
            
            
    
        
