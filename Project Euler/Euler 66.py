#!/usr/bin
d_count = []
d_range = 5
for d in range(1, d_range):
    for x in range(1, d_range * 5):
        for y in range(1, round((x / (d ** 0.5)) + 1)):
            print(x,y,d,x**2 - d * y**2)
            if x in d_count:
                continue
            if x**2 - d * y**2 == 1:
                d_count.append(x)
print(max(d_count), d_count)