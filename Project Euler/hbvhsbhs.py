n = 7
walls = list(map(int, "3 6 7 1 3 8 2".split(" ")))
maxa = 0
c = 0
for i in walls:
    c += 1
    b = c
    for j in walls[c:]:
        b +=1
        print(i,j,abs( b - c))
        if min(i,j) * abs( b - c) > maxa:
            maxa = min(j ,i) * abs( b - c)
print(maxa)