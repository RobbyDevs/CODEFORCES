for w in range(int(input())):
    
    n, a,b = map(int,input().split())
    
    
    if ((max(a,b)-min(a,b))-1) == 0:
        print('NO')
    elif ((max(a,b)-min(a,b))-1) %2 == 0:
        print('NO')
    else:
        print('YES')