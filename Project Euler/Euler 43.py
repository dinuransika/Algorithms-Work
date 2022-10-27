import itertools
a=(list(itertools.permutations([0,1,2,3,4,5,6,7,8,9])))
b=(2,3,5,7,11,13,17)

for i in a:
    m=1
    val=0
    while m!=8:
        q=0
        su=0
        for j in (i[m+2],i[m+1],i[m]):
            su+=j*(10**q)
            q+=1
        if su%(b[m-1])==0:
            val+=1
        m+=1
    if val==7:
        print i
    
