for w in range(int(input())):
    #n = int(input())
    v = list(map(int,input().split()))
    
    va = [abs(x) for x in v]
    
    va.sort()
    
    v0 = v[0]
    
    
    print(v)
    print(va)
