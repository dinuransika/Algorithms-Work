prime=28433
for i in range(1,7830458):
    prime*=2
    prime=prime%(10**10)

print(prime+1)
    
    
