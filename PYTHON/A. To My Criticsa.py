for w in range(int(input())):
    v = list(map(int,input().split()))
    
    v.sort()
    
    if v[1]+v[2] >=10:
        print('YES')
        
    else:
        print('NO')