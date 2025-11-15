for w in range(int(input())):
    
    n,k = map(int,input().split())
    
    v = list(map(int,input().split()))
    
    v.sort()
    

    fatia = v.pop()
    
    c = 0
    
    
    for i in range(k-1):
        if fatia >= n:
            break
        
        if v[i] == 1:
            c+=1
            fatia +=1
            
        else:
            
            if v[i]+fatia <= n:
                c+= (v[i]-1) + v[i]
                fatia +=v[i]
                
            else:
                c+=v[i]*2
                fatia +=v[i]
    print(c)