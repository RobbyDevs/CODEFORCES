for w in range(int(input())):
    dic = [1,2,3,4,5,5,4,3,2,1]
    
    m = []
    for i in range(10):
        m.append(input())
        
    v = []
    c = 0
    a = b = 0
    for i in range(10):
        for j in range(10):
            if m[i][j] == 'X':
                v.append(min(dic[i],dic[j]))
                
    for i in v:
        c += dic[i-1]
    print(c)
    

