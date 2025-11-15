for w in range(int(input())):
    n = int(input())
    v = list(map(int,input().split()))
    
    men = min(v)
    ans = 0
    for i in v:
        if i>men:
            ans+= i-men
            
            
    print(ans)