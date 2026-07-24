def solve():
    n, k = map(int,input().split())
    va = list(map(int,input().split()))
    vb = list(map(int,input().split()))
    
    flag = 0
    
    for i in range(n):
        if (va[i]<vb[i]):
            flag = 1
        
    ans = 0
    if (flag):
        va.sort()
        vb.sort()
        for i in range(n):
            if (vb[i]>va[i]):
                print(-1)
                return
            else:
                ans+= va[i]-vb[i]
        print(k+ans)
    else:
        ans1 = 0
        ans2 = k
        for i in range(n):
            ans1+= va[i]-vb[i]
        
        va.sort()
        vb.sort()
        
        for i in range(n):
            if (vb[i]<va[i]):
                ans2 = 1000000000000000000
                break
            else:
                ans2+= vb[i]-va[i]
        print(min(ans1,ans2))
        
        
for w in range(int(input())):
      solve()
            
            