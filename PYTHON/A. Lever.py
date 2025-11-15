for w in range(int(input())):
    n = int(input())
    
    va = list(map(int,input().split()))
    vb = list(map(int,input().split()))
    
    ans = 1
    flag = 0
    
    
    for i in range(n):
        if va[i]>vb[i]:
            ans+= va[i]-vb[i]
            
    print(ans)
"""
1 8 1 9 7 1

1 9 1 9 8 1

6
"""
