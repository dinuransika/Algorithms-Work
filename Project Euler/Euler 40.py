from time import time
start=time()
fo=open("Euler 40.txt","w+")

for i in range(1,10000000):
    fo.write(str(i))
fo.seek(0)
strl=fo.read()
sumnum=1
n=0
for i in strl:
    n+=1
    if n==1 or n==10 or n==100 or n==1000 or n==10000 or n==100000 or n==1000000:
        sumnum*=int(i)
        #print i
        #print n
fo.close()
print(sumnum)
print(time()-start)
