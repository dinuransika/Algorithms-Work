from time import time
from sys import exit


start = time()
for i in range(1000000070, 1414213562, 100):
    sq = list(str(i**2))
    if sq[2] == "2" and sq[4] == "3" and sq[6] == "4" and sq[8] == "5" and sq[10] == "6" and sq[12] == "7" and sq[14] == "8" and sq[16] == "9":
        print(i)
        print(time()-start)
        exit()

for i in range(1000000030,1414213562,100):
    sq=list(str(i**2))
    if sq[2] == "2" and sq[4] == "3" and sq[6] == "4" and sq[8] == "5" and sq[10] == "6" and sq[12] == "7" and sq[14] == "8" and sq[16] == "9":
        print(i)
        print(time()-start)
        break
    
