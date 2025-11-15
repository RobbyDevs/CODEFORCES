for w in range(int(input())):
    
    a,b = map(int,input().split())
    
    
    if a == 0:
        if b %2 != 0:
            print('NO')
        else:
            print('YES')
        
    elif b == 0:
        if a % 2 != 0:
            print('NO')
        else:
            print('YES')
        
    else:
        
        bb = b + (a//2)
        aa = a%2
        if ((bb*2) + aa) %2 == 0:
            print('YES')
        else:
            print('NO')