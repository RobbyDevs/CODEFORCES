for w in range(int(input())):
    
    n,k = map(int,input().split())
    
    va = []
    vb = []
    if k == 1:
        print('YES')
        print(n)
        
    else:
        for i in range(k-1):
            va.append(1)
        va.append(n-(i+1))
        
        for i in range(k-1):
            vb.append(2)
        vb.append(n-((i+1)*2))
    
        
        if len(va) + len(vb) == 0:
            print('NO')
        else:
            
            if va[-1]%2 == va[0]%2 and va[-1]>0:
                print('YES')
                print(*va,sep=' ')
                
            elif vb[-1]%2 == vb[0]%2 and vb[-1]>0:
                print('YES')
                print(*vb,sep=' ')
            else:
                print('NO')