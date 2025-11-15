for w in range(int(input())):
    
    n,m = map(int,input().split())
    
    va = [str(x) for x in input()]
    
    vi = sorted(list(map(int,input().split())))
    
    vb = [str(x) for x in input()]
    vb.sort()
    
    print()
    
    print(vb)
    print(vi)
    ind = 0
    for i in range(m):
        if vb[ind]<=va[vi[i]-1]:
            
            va[vi[i]-1] = vb[ind]
            ind+=1
        
            
        #print(vb[i],end=' ')
    print()
    print(va)

