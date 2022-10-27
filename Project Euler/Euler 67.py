from time import time
start=time()
fo=open("Euler 67.txt","r")
li=[]
for i in fo: li.append([int(j) for j in i.split(" ")])
a=99
ls=list(li)
while a!=0:
    for i in range(0,len(li[a])-1): li[a-1][i]+=max(li[a][i],li[a][i+1])
    a-=1
print(li[0])
fo.close()
print(time() - start)
