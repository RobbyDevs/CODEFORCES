for w in range(int(input())):
    
    n = int(input())
    v = list(map(int,input().split()))
    
    c0 =c1 = 0
    if sum(v) == n:
        print('YES')
    else:
        for i in range(n-1):
            if v[i] == 0:
                c0+=1
            else:
                c1+=1
                
            if (v[i]+v[i+1] == 0):
                print('YES')
                break
        
        else:
            print('NO')