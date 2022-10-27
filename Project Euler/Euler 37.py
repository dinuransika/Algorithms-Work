def Prime(x):
    if x<2:
        return False
    elif x==2 or x==3:
        return True
    else:
        i=1
        while i<int(x**0.5+1):
            i+=1
            if x%i==0:
                return False
                break
            else :
                continue
        else:
            return True
i=10
suma=0
while i<1000000:
    i+=1
    if Prime(i)==True:
        ic=i
        icc=i
        t=1
        while ic!=0:
            ic//=10
            if Prime(ic)==True:
                t+=1
        diga=len(str(icc))
        digac=diga
        t+=1
        while diga!=0:
            diga-=1
            if Prime(icc%(10**diga))==True:
                t+=1
        if t==(digac*2):
            suma+=i
            print i
print suma                
          
        
  
            
            
        
    
