for w in range(int(input())):
    
    n = int(input())
    
    va = list(map(int,input().split()))
    vb = []
    vc = []
    
    mai = max(va)
    nmai = 0
    con = 0
    va.sort()
    
    for i in range(n):
        if va[i] == mai:
            nmai +=1
            
        else:
            con = 1
            
    
    if con == 0:
        print(-1)
    
    else:
        #print('>>')
        
        for i in range(nmai):
            va.pop()
            
        print(len(va),nmai)
        print(*va,sep=' ')
        for i in range(nmai):
            print(mai,end= ' ')
            
        print()