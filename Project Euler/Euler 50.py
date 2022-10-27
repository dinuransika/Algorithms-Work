def prime(x):
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

j=0
k=0
su=0
sums=[]
while k<1000:
    k+=1
    if prime(k)==True:
        j=k
        while su<9999980:
            j+=1
            su=0
            if prime(j)==True:
                su+=j
                if prime(su)==True:
                    sums.append(su)

print(max(sums))
                    
                    


        


