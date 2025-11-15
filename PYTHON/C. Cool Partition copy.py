for w in range(int(input())):
    
    n = int(input())
    v = list(map(int,input().split()))
    

    d1 = {}
    d2 = {}
    ind = 0
    ans = 1
    flag= 0
    
    for i in range(n):
        if v[i] not in d1:
            d1[v[i]] = 1
        
        else:
            ind = i
            flag =1 
            break
        
    if flag == 0:
        print(ans)
    else:
        
        flag = 0
        
        for i in range(ind,n):
            if v[i] not in d2:
                d2[v[i]] = 1
                
            
                
            
                
            if v[i] in d1:
                d1.__delitem__(v[i])
            #print(len(d1))
            if len(d1) == 0:
                d1 = dict(d2)
                d2.clear()
                ans+=1
                
        print(ans)
        
