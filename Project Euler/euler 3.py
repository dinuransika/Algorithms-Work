x = 13195
i=0
j=0
su=0
while i<x:
   i = i+1
   if x%i==0:
       while j<i:{
           j=j+1
           if i%j==0:
               su=su+j}
       if su==1:
           print(i)
       su=0
       j=0
            
        
            
               
