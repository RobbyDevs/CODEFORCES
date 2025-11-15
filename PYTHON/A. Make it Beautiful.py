for w in range(int(input())):
    n = int(input())
    v = list(map(int,input().split()))
    
    item = v[0]
    for i in v:
        if item != i:
            break
    else:
        print('NO')
        continue
    
    
    v.sort()
    
    v.insert(0,v.pop())
    
    print('YES')
    print(*v,sep=' ')
    
    
