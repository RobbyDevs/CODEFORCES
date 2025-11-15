def solve():
    s,n = map(int,input().split())
    v = []
    
    for i in range(n):
        
        v.append(list(map(int,input().split())))
        
        
    v.sort(key= lambda x: (x[0],-x[1]))
    
    #print(v)
    for par in v:
        if s> par[0]:
            s+=par[1]
        else:
            print("NO")
            return
        
    #print(v)
    
    print("YES")
    return

solve()