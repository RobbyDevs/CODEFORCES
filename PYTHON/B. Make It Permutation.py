for w in range(int(input())):
    
    n = int(input())
    ma = []
    
    for i in range(n):
        va = [x for x in range(1,n+1)]
        ma.append(va)
        
    #print(*ma,sep='\n')
    
    
    va = []
    vb = []
    saida = []
    ans = 0
    e1 = 1
    d1 = n #dim
    
    e2 = n #aum
    d2 = n 
    saida.append([1,e1,d1])
    
    ans+=1
    d1-=1
    e2-=1
    for i in range(2,n+1):
        if d1-e1>=1:
            saida.append([i,e1,d1])
            ans+=1
        if d2-e2>=2:
            saida.append([i,e2+1,d2])
            ans+=1
        d1-=1
        e2-=1
            
    print(ans)
    for i in saida:
        print(*i,sep=' ')
