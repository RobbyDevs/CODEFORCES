for w in range(int(input())):
    n = int(input())
    
    v = []
    for i in range(n):
        a,b = input().split()
        v.append([int(a),int(b[0]),int(b[1])])
    
        
    v.sort(key= lambda x: (x[0],-x[1],-x[2]))
    
    #print(v)
    
    c = 0
    s = 0
    p1 = 0
    p2 = 0
    p3 = 0
    for i in range(len(v)):
        if (v[i][1] == 1 and v[i][2] == 0) and p1 == 0:
            p1 = list(v[i])
            
        if (v[i][2] == 1 and v[i][1] == 0) and p2 ==0:
            p2 = list(v[i])
        if v[i][1] == 1 and v[i][2]==1 and p3 == 0:
            p3 = list(v[i])
    
    #print('>>')
    #print(p1,p2,p3)
    
    if p3 == 0:
        
        if p1 == 0 or p2 == 0:
            print(-1)
            
        else:
            
            if p1 == p2:
                print(p1[0])
            else:
                print(p1[0]+p2[0])
    else:
        if p1 == 0 or p2 == 0:
            print(p3[0])
        else:
            if p3[0] <= (p1[0]+p2[0]):
                print(p3[0])
            else:
                if p1 == p2:
                    print(p1[0])
                else:
                    print(p1[0]+p2[0])