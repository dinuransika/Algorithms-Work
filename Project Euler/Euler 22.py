fo=open("Euler_22.txt","r")
strl=fo.read()
fo.close()
lets=0
letsall=0
count=0
for i in strl[:]:
    if i!=",":
        if i=="A":
            lets+=1
        elif i=="B":
            lets+=2
        elif i=="C":
            lets+=3
        elif i=="D":
            lets+=4
        elif i=="E":
            lets+=5
        elif i=="F":
            lets+=6
        elif i=="G":
            lets+=7
        elif i=="H":
            lets+=8
        elif i=="I":
            lets+=9
        elif i=="J":
            lets+=10
        elif i=="K":
            lets+=11
        elif i=="L":
            lets+=12
        elif i=="M":
            lets+=13
        elif i=="N":
            lets+=14
        elif i=="O":
            lets+=15
        elif i=="P":
            lets+=16
        elif i=="Q":
            lets+=17
        elif i=="R":
            lets+=18
        elif i=="S":
            lets+=19
        elif i=="T":
            lets+=20
        elif i=="U":
            lets+=21
        elif i=="V":
            lets+=22
        elif i=="W":
            lets+=23
        elif i=="X":
            lets+=24
        elif i=="Y":
            lets+=25
        elif i=="Z":
            lets+=26
        else:
            lets+=0
    else:
        count+=1
        letsall+=lets*count
        lets=0
        

print(letsall)
    
        
