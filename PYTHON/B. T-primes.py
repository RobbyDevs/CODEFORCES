from math import log

w = int(input())

v=  list(map(int,input().split()))

for i in v:
    if i == 1:
        print('NO')
        
    else:
        
        a = int(i**(1/2))
        
        if a*a == i:
            print('YES')
        else:
            print('NO')