for w in range(int(input())):
    
    n = int(input())
    
    v = list(map(int,input().split()))
    c = 0
    for i in range(n-1):
        mi, ma = min(v[i],v[i+1]),max(v[i],v[i+1])
        d = ma - (2*mi)
        
        while d >0:
            d = ma - (2*mi)
            mi = 2*mi
            c+=1
    print(c)