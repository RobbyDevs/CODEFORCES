for w in range(int(input())):
    
    n = int(input())
    v = list(map(int,input().split()))
    

    s1 =set()
    s2 = set(v)
    
    ind = 0
    ans = 1
    flag= 0
    
    for i in range(n-1,-1,-1):
        if len(s1)<len(s2):
            s1.add(v[i])
            
        else:
            ans+=1
            s2 = set(s1)
            s1.clear()

                
                
    print(ans)
    print('^^^^')