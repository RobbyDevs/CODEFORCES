for w in range(int(input())):
    
    l,r = map(int,input().split())
    L,R = map(int,input().split())
    
    lmin,lmax = min(l,L),max(l,L)
    rmin,rmax = min(r,R),max(r,R)
    
    
    v = [0 for i in range(100)]
    
    #print(v)
    
    for i in range(l,r+1):
        v[i-1] +=1
    for i in range(L,R+1):
        v[i-1]+=1
    c = 0
    for i in range(100):
        if v[i] == 2:
            if i >0:
                if v[i-1] !=0:
                    c+=1
            if i <99:    
                if v[i+1] == 1:
                    c+=1
              
    if c == 0:
        print(1)
    else:
        print(c)