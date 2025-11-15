for w in range(int(input())):
    n = int(input())
    
    v = list(map(int,input().split()))
    
    if len(v) == 1:
        #print('>>>')
        if sum(v) == 0: print(1)
        else: print(0)
        
    else:
        s = 0
        vs = [0]
        for i in range(n):
            vs.append(v[i]+vs[i])
            
        c = 0
        vs.pop(0)
        print(vs)
        
        for i in range(len(vs)):
            if i 
            
            
        
        print(c)    
    print('>>>>')

