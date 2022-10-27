def Permutation(x):
    nums=['1','2','3','4','5','6','7','8','9','0']
    xc=x
    nu=[]
    while xc!=0:
        rema=xc%10
        nu.append(str(rema))
        xc//=10
    diga=set(nums) & set(nu)
    if len(diga)==len(nums):
        return True
    else:
        return False

t=1088640
n=3000000000
while n<5000000000:
    n+=1
    if Permutation(n)==True:
        t-=1
    if t==1000000:
        print n
        break
    


    
         

