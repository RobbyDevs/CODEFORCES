for w in range(int(input())):
    k,n = map(int,input().split())
    
    ad = 0
    pont = 0
    v = [1]
    ind = 0
    for i in range(1,n+1):
        ad+=1
        
        if len(v) == k:
            break
        
        
        else:
            pont = v[-1]+ad
            
            if pont <= n:
                v.append(pont)
                
    if v[-1]+1 <= n:
        for i in range(v[-1]+1,n+1):
            if len(v)<k:
                v.append(i)
            else:
                break

    
    
    #print(v)
    while len(v)<k:
        for i in range(len(v)-2,-1,-1):
            if v[i+1]-v[i]>1:
                v.insert(i+1,v[i]+1)
                break
            
    #print(v)
    
    #print(len(v))
    print(*v,sep=' ')
