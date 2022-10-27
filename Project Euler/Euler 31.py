p1=1
p2=2
p5=5
p10=10
p20=20
p50=50
p100=100
p200=200

su=200
j=0
z=0
while j<3:
    k=0
    while k<5:
        l=0
        while l<11:
            m=0
            while m<21:
                n=0
                while n<41:
                    q=0
                    while q<101:
                        r=0
                        while r<201:
                            if p100*j+p50*k+p20*l+p10*m+p5*n+p2*q+p1*r==su:
                                z+=1
                            r+=1
                        q+=1
                    n+=1
                m+=1
            l+=1
        k+=1
    j+=1



print(z)

                
                           
    
