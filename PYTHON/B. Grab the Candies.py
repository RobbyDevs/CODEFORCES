for w in range(int(input())):
    n = int(input())
    sp=si =0
    v = list(map(int,input().split()))
    
    for i in v:
        if i %2 == 0:
            sp +=i
        else:
            si +=i
            
    if sp > si:
        print('YES')
    else:
        print('NO')