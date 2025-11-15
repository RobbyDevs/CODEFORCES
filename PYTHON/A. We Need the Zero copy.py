for w in range(int(input())):
    n = int(input())
    
    v = list(map(int,input().split()))
    vb = [bin(x)[2:] for x in v]
    
    
    p = int(input())
    
    vc = []
    for i in vb:
        vc.append(int(i)^p)
    
    c = 0
    for i in vc:
        c^= i
        
    print(vb)
    print(vc)
    print(c)