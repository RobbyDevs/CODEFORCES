
for w in range(int(input())):
    
    n,k = map(int,input().split())
    
    dic = {}
    v = input()
    

    for i in v:
        
        try:
            dic[i]+=1
        except KeyError:
            dic[i] = 1
    par  = 0
    imp = 0
    for i in dic.values():
        if i %2 == 0:
            par+=1
            
        else:
            imp +=1
        

    if (n - k) %2 == 0:
        #print(k-imp)
        if imp <= k:
            print('YES')
        else:
            print('NO')
            
    else:
        
        if imp <= k+1:
            print('YES')
        else:
            print('NO')

