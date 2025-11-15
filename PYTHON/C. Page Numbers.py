for w in range(int(input())):
    
    n = int(input())
    
    v = list(map(int,input().split()))
    
    ans = [[v[0]]]
    
    for i in range(n-1):
        if v[i+1]-v[i]>1:
            ans.append(v[i])
    print(len(ans))