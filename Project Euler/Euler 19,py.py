#!/usr/bin
ny=[31,28,31,30,31,30,31,31,30,31,30,31]
ly=[31,29,31,30,31,30,31,31,30,31,30,31]
y=1900
date=[]
while y<1901:
    if y%400==0 or y%4==0:
        for i in ly:
            for j in range(1,i+1):
                date.append(j)
    else:
        for i in ly:
            for j in range(1,i+1):
                date.append(j)
    y+=1
a=7
sunc=0
for i in range(1,int(len(date)/7)):
    a+=7
    if date[a]==1:
        sunc+=1
print(sunc)

