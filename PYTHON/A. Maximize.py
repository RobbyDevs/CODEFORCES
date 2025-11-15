from math import gcd

for w in range(int(input())):
    
    n = int(input())
    
    for i in range(2,(n//2)+1):
        if n%i == 0:
            print(n-i)
            break
    else:
        print(n-1)