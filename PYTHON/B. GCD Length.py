from math import gcd

for w in range(int(input())):
    
    a,b,c = map(int,input().split())
    
    x = y = 0
    
    d = 10**(c-1)
    
    x = d * (10**(a-c))
    y = d * (10**(b-c))
    
    if a > c and b > c:
        x+=1
        y+=1
    
    print(x, y)
    print(gcd(x,y))