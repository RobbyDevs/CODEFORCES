for w in range(int(input())):
    
    n = int(input())
    
    v = list(map(int,input().split()))
    c = 0
    for i in range(n-1):
        mi, ma = min(v[i],v[i+1]),max(v[i],v[i+1])
        d = ma - (2*mi)
        #print(d)
        while d >0:
            c+=1
            mi = 2*mi
            d = ma - (2*mi)
    print(c)