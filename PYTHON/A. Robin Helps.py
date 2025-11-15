for w in range(int(input())):
    n,k = map(int,input().split())
    v = list(map(int,input().split()))
    mo = c = 0
    
    for i in v:
        if i >= k:
            mo+=i
                        
        elif i == 0 and mo >0 :
            c+=1
            mo -=1
            
    print(c)