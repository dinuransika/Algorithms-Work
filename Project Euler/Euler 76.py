#!/usr/bin
from time import time
start = time()
li = [1,2,3,4,5,6]
num = len(li)
num_list = [1] + [0] * num
for i in li:
    for j in range(i, num+1):
        num_list[j] += num_list[j-i]
print(num_list[num])
print(time()-start)
