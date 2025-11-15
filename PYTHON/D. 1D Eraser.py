for w in range(int(input())):
    
    n,k = map(int,input().split())
    
    v = [str(x) for x in input()]
    c = 0
    
    if n<=k:
        if 'B' in v:
            
            print(1)
        else:
            print(0)
    else:
        
        for i in range(n-k):
            
            if v[i] == 'B':
                
                for j in range(i,i+k):
                    if v[j] == 'B':
                        v[j] = 'W'
                        
                    i = j
                c+=1
        else:
            if 'B' in v[(n-k-1):]:
                c+=1
        print(c)