from time import time


def isPrime(n):
  
    # Corner cases 
    if n <= 1:
        return False
    if n <= 3:
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if n % 2 == 0 or n % 3 == 0:
        return False
  
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
  
    return True


start = time()
su1 = 0
for k in range(1, 2000000, 2):
    if isPrime(k) == 1:
        su1 += k
print(su1)
print(time() - start)
