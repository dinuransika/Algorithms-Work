#!/usr/bin
import time

start = time.time()
cube_list = []
count = 0
while True:
    cube = list(str(count ** 3))
    cube.sort()
    cube_list.append(cube)
    if cube_list.count(cube) == 5:
        print(cube_list.index(cube))
        break
    count += 1
print(time.time() - start)
