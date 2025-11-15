for w in range(int(input())):
    n = int(input())
    
    va = list(map(int,input().split()))
    vb = list(map(int,input().split()))
    
    
    m = int(input())
    
    vd = list(map(int,input().split()))
    dic = {}
    
    for i in range(n):
        if vb[i]!=va[i]:
            try:
                
                dic[vb[i]]+=1
            except KeyError:
                dic[vb[i]]= 1
                
    for i in range(m):
        try:
            dic[vd[i]]-=1
        except KeyError:
            dic[vd[i]] = 0
    
    flag = 0
    if vd[-1] in vb:
        flag = 1
        
    
    if flag ==1:
        for i in dic.values():
            if i >0:
                flag = 0
    
    if flag == 1:
        print('YES')
    else:
        print("NO")
        
    