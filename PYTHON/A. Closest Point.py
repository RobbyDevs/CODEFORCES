for w in range(int(input())):
    
    n = int(input())
    v = list(map(int,input().split()))
    
    if len(v)==2:
        if abs(v[0]-v[1]) >1:
            print('YES')
        else:
            print('NO')
            
    else:
        print("NO")