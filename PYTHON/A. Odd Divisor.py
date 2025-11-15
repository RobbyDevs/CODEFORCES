from math import log2
for w in range(int(input())):
    
    n = int(input())
    
    if (n%2 !=0):
        print('YES')
    else:
        a = log2(n)
        if a - int(a) == 0:
            print('NO')
        else:
            print('YES')
        