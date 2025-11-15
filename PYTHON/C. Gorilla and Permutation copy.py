for w in range(int(input())):
    n,m,k = map(int,input().split())
    
    v = [int(x) for x in range(n,m,-1)]
    
    
    for i in range(1,m+1):
        v.append(i)
    print(*v,sep=' ')
