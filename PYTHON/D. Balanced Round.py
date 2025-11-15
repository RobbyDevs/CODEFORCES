for w in range(int(input())):
    
    n,k = map(int,input().split())
    
    v = sorted(list(map(int,input().split())))
    #print(v)
    c = 1
    va = [0]
    me = n//2
    for i in range(n-1):
        if v[i+1]-v[i] >k:
            va.append(c)
            c = 1
            
        else:
            c+=1
    else:va.append(c)
    #print(va)
    print(n-max(va))