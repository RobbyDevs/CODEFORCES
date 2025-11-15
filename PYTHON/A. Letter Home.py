for w in range(int(input())):
    n,s = map(int,input().split())
    v = list(map(int,input().split()))
    
    
    if s>=v[-1]: #ok
        dir = 0
        esq = s-v[0]
        
    elif s<=v[0]:
        
        dir = v[-1]-s
        esq = 0
    else:
        esq = s-v[0]
        dir = (v[-1] - s)
    
    #print(esq,dir)
        
    total = (min(esq,dir)*2) + max(esq,dir)
    print(total)
    #print('^^^')
    
