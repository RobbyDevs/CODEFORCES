for w in range(int(input())):
    
    n,k = map(int,input().split())
    
    v = list(map(int,input().split()))
    
    va = []
    ni=np = 0
    for i in v:
        if i%2 == 0:
            np +=1
        else:
            ni+=1
            
    if k == 2:
        if np == 0:
            print(1)
        else:
            print(2)
    elif k == 4:
        if np == 2:
            print(0)
        elif np == 1:
            print(1)
        else:
            print(2)
    else:
        dif = 100
        for i in v:
            if i >= k and i%k <dif:
                dif = i%k
            else:
                if i% k == 0:
                    dif = 0
                    
                else:
                    j = (i//k) +1
                    if  (k*j) %i  < dif:
                        dif = (k*j) %i
                        
        print(dif)