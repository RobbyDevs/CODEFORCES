for w in range(int(input())):
    
    n,ma = map(int,input().split())
    
    m = []
    s = 'vika'
    for i in range(n):
        m.append(input())
        
    k = 0
    c = 0
    for i in range(ma):
        for j in range(n):
            if k < 4:
                if m[j][i] == s[k]:
                    #print(m[j][i], s[k])
                    k+=1
                    break
            else: 
                c +=1
                break
        if c >0:
            break 
            
    #print(k)
    if k < 4:
        print('NO')
    else:
        print('YES')