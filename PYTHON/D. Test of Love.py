for w in range(int(input())):
    n,m,k = map(int,input().split())
    m-=1
    k-=1
    v = input()
    
    vf = [0,'']*(len(v)+1)
    
    ant = ''
    ind = 0
    
    for i in v:
        if i != "L":
            if i == ant:
                vf[ind]+=1
            else:
                ind +=1
                ant = i
                vf[ind] = 1
        else:
            ind+=1
            
    print(vf)
    pulando = nadando = 1
    for i in vf:
        if i > m:
            pulando = 0
        if i > k:
            nadando = 0
    
    if pulando + nadando ==0:
        print('NO')
    else:
        print('YES')
    
    
        