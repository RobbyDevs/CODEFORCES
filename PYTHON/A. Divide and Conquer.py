from math import gcd

def div(n):
    v = []
    i = 1
    while i*i<=n:
        if n%i ==0:
            v.append(i)
        
            if (i != n//i):
                v.append(n//i)
        i+=1
    
    return v
    
for w in range(int(input())):
    a,b = map(int,input().split())
    
    if b in div(a):
        print("YES")
    else:
        print("NO")

    