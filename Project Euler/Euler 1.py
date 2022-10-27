import time
start=time.time()
i = 0
sum1 = 0
while i<1000:
    if i%3==0 or i%5==0 :
        sum1 = sum1 +i
    i = i +1
print(sum1)
end=time.time()
print end-start
