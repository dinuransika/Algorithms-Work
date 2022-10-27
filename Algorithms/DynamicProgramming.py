def CutRod(p, n):
    if n==0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i-1]+CutRod(p, n-i))
    return q

a = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(CutRod(a, 1))