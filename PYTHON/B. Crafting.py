for w in range(int(input())):
    
    n = int(input())
    
    va = list(map(int,input().split()))
    vb = list(map(int,input().split()))
    vd = []
    nneg  = 0
    menposi = 1000000000
    falta = 0
    tenho = 0
    for i in range(n):
        dif = va[i]-vb[i]
        
        vd.append(dif)
        if dif <0:
            falta += dif
            nneg+=1
        if dif > tenho:
            tenho = dif
            
    for i in range(n):
        if vd[i] >0 and vd[i]<menposi:
            menposi = vd[i]
            
        
    #print(vd)
    #print(tenho, falta)
    if  >= nneg*(-falta):
        print('YES')
    else:
        print('NO')
        
#maior positivo deve ser maior ou igual a qtd n neg