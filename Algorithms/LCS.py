def LCS_Length(X, Y):
    m = len(X)
    n = len(Y)
    c = [[None]*(n+1) for i in range(m+1)]
    b = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                    c[i][j] = 0
            elif X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = 0
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 1
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 2
    return c[m][n], b

def PrintLCS(b, X, i, j):
    if i==0 or j==0:
        return
    if b[i][j] == 0:
        PrintLCS(b, X, i-1, j-1)
        print(X[i-1], end='')
    elif b[i][j] == 1:
        PrintLCS(b, X, i-1, j)
    else:
        PrintLCS(b, X, i, j-1)

X = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
Y = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
# print(LCS_Length(X, Y))
i, b = LCS_Length(X, Y)
PrintLCS(b, X, len(X), len(Y))