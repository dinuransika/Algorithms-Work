from time import time
from math import gcd
from functools import reduce
start = time()
N = 20
print(reduce(lambda x,y:x*y//gcd(x,y), range(1, N+1)))
print(time() - start)
   
