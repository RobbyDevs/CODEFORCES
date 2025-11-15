for w in range(int(input())):
    n = int(input())
    
    v = list(map(int,input().split()))
    
    p = 0
    while p <=256:
        vc = []
        for i in v:
            vc.append(p^i)
        
        c = 0
        for i in vc:
            c^=i
        
        if c==0:
            print(p)
            break
        p+=1
    else:
        print(-1)