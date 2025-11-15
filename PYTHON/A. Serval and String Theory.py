for w in range(int(input())):
    
    l, n = map(int,input().split())
    
    v = [str(x) for x in input()]
    
    vr = list(reversed(v))
    
    
    if n == 0:
        if vr>v:
            print('YES')
        else:
            print('NO')
            
            
    else:
        vant = v[0]
        for i in v:
            if i != vant:
                print('YES')
                break
        else:
            print('NO')