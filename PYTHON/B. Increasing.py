for w in range(int(input())):
    
    n = int(input())
    
    v = list(map(int,input().split()))
    if n ==1:
        print('YES')
        
    else:        
        v.sort()
        for i in range(n-1):
            if v[i+1] <= v[i]:
                print('NO')
                break
        else:
            print('YES')