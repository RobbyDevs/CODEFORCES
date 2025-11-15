for w in range(int(input())):
    
    n,k = map(int,input().split())
    
    v = sorted(list(map(int,input().split())))
    
    dic = {}
    for i in range(n):
        try:
            dic[v[i]] +=1
        except KeyError:
            dic[v[i]] = 1
    
    #print(v)
    #print(dic)
    
    c =0
    for chave,valor in dic.items():
        
        try:
            c += min((valor,dic[k-chave]))
            
        except KeyError:
            pass
    #print('vvvvv')
    print(c//2)