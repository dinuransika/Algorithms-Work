
x = 1
y = 2
y1 = 0
sum1 = 0
while y<4000000:
    if y%2==0:
        sum1 = sum1  + y
    y1 = y
    y = x + y
    x = y1
    
print(sum1)
    
