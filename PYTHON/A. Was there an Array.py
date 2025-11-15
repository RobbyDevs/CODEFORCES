for w in range(int(input())):
    
    n = int(input())
    
    v = list(map(str,input().split()))
    v = ''.join([str(x) for x in v])
    
    
    #print(v)
    if '101' in v:
        print('NO')
    else:
        print('YES')