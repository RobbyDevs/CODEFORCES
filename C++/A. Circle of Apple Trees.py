for w in range(int(input())):
    
    n = int(input())
    v = list(map(int,input().split()))
    
    v.sort()
    
    #print(v)
    
    ans = 0
    ant = 0
    
    for i in v:
        if i >ant:
            ans+=1
            ant = i
    
    print(ans)