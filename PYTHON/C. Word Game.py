for w in range(int(input())):
    
    n = int(input())

    dic = {}
    vp =[0,0,0]
    for i in range(3):
        for j in input().split():
            try:
                dic[j][1]+=1
                if i not in dic[j][0]:
                    dic[j][0].append(i)
            
            except KeyError: dic[j]=[[i],1]
        
    
    for valor in dic.values():
        if valor[1] == 1:
            vp[valor[0][0]]+=3
        elif valor[1] ==2:
            for i in valor[0]:
                vp[i]+=1
        
    print(*vp,sep=' ')