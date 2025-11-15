for w in range(int(input())):
    
    n = int(input())
    v = [str(x) for x in input()]
    
    pilha = []
    
        
    val = []
    
    s = 0
    
    #print(*v,sep='')
    
    
    for i in range(n):
        if i % 2 ==0:
            if len(val) == 0:
                val.append(i)
                
            else:                
                s+= i-val[-1]
                val.pop()
        
            
        else:
            if v[i] == '(':
                val.append(i)
            else:
                s+= i-val[-1]
                val.pop()
                
    
    #print(*v,sep='')
    print(s)
    
