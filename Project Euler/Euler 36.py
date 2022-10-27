from Eulerfunc import *


i=0
su1=0
while i<4000:
    i+=1
    if palindromic(i)==True:
        dec=i
        su=0
        pw=-1
        while dec!=0:
            rema=dec%2
            pw+=1
            su+=rema*pow(10,pw)
            dec//=2
        if palindromic(su)==True:
            su1+=i
print(su1)
            
    
    
    
    
        
