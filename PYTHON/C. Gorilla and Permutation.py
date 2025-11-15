for w in range(int(input())):
    n,m,k = map(int,input().split())
    
    v = [int(x) for x in range(1,n+1)]
    
    v.sort(reverse= True)
    
    vs = [0]
    
    gi = 0
    for i in range(n):
        vs.append(vs[i]+v[i])
        if v[i] >=k:
            gi+=v[i]

    gi = gi*n
    
    for i in range(n):
        
        
        
    print(vs)