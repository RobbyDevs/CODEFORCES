def solve():
    n = int(input())
    
    v = list(map(int,input().split()))
    
    mai = max(v)
    flag = n
    
    if n <=2 :
        print(mai)
        return
    
    while sum(v) >0:
        mai = max(v)
        prox = 0
        print(flag)
        print(v)
        if flag <= 0:
            break
        
        for i in range(n):
            if v[i] == mai:
                if i ==0:
                    prox = v[i+1]
                elif i == n-1:
                    prox = v[n-2]
                    
                else:
                    prox = max(v[i+1],v[i-1])
                    
                flag -= abs(mai-prox)
                v[i] = prox
                break
                    
    if flag >=0:
        print("YES")
    else:
        print("NO")
    
    
    
for w in range(int(input())):
    
    solve()
    
    
"""
5
1 5 3 4 2

2
"""    
