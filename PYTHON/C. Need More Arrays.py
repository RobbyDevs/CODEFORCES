for w in range(int(input())):
    n = int(input())
    v = list(map(int,input().split()))
    
    ans = [v[0]]
    
    for i in range(1,n):
        if v[i]-ans[-1]>1:
            ans.append(v[i])
    print(len(ans))