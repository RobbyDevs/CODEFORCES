for w in range(int(input())):
    
    a,b,c,d = map(int,input().split())
    a,b = min(a,b),max(a,b)
    c,d = min(c,d),max(c,d)
    
    va = [x for x in range(a,b+1)]
    vb = [x for x in range(c,d+1)]
    
    
    flag1=flag2=flag3=flag4=0
    if va[0] not in vb:
        flag1 = 1
        
    if va[-1] not in vb:
        flag2 = 1
        
    if vb[0] not in va:
        flag3 = 1
    if vb[-1]not in va:
        flag4 = 1
        
    if flag1+flag2 == 1 or flag3+flag4 ==1:
    
        print('YES')
    else:
        print("NO")
    print(va)
    print(vb)