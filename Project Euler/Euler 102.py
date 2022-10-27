#!/usr/bin
from time import time
start =time()
fo = open("p102_triangles.txt", "r")
count = 0
for lines in fo.readlines():
    ax, ay, bx, by, cx, cy = map(int, lines.split(","))
    A = ax * by - bx * ay > 0
    B = ax * cy - ay * cx > 0
    C = cx * by - cy * bx > 0
    if A == B == C :
        count += 1
fo.close()
print(count)
print(time() - start)
