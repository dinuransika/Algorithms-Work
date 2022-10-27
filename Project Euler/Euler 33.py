#!/usr/bin
pro=1
for i in range(11,100):
    for j in range(11,100):
        seti=set(str(i))
        setj=set(str(j))
        if i>j and seti!=setj and i%11!=0 and j%11!=0:
            mem=j/i
            comm=seti&setj
            if comm!={'0'}:
                if len(seti)==2:
                    nli=list(seti-comm)
                else:
                    nli=list(seti)
                if len(setj)==2:
                    nlj=list(setj-comm)
                else:
                    nlj=list(setj)
                if int(nli[0])!=0 and int(nlj[0])/int(nli[0])==mem:
                    pro*=int(nli[0])
                    print(int(nlj[0]),int(nli[0]),mem,j,i)
print(pro)
