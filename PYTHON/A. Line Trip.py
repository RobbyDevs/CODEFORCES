ct = int(input())

for w in range(ct):
    
    n,x = map(int,input().split())

    v = list(map(int,input().split()))
    a = v[0]
    
    for i in range(n):
        j = i+1
        
        if i < n-1:
            if v[j]-v[i] > a:
                a = v[j] - v[i]
        
    if (x - v[n-1])*2 > a:
        a = (x - v[n-1])*2
    
    
    print(a)