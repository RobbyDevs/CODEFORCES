from math import gcd

for w in range(int(input())):
    
    n = int(input())
    
    v = list(map(int,input().split()))
   
    c =0
    
    va = []
    
    
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            
            if v[i] % 2 == 0:
                if v[j]%2 == 0:
                    continue 
            if v[i] % 3 == 0:
                if v[j]%3 == 0:
                    continue
            if v[i] % 5 == 0:
                if v[j]%5 == 0:
                    continue
            
            
            if gcd(v[i],v[j]) == 1:
                if c < i+j:
                    c=i+j
    
    if c == 0:
        print(-1)
    else:
        print(c+2)