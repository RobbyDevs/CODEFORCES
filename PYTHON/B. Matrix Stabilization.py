for w in range(int(input())):
    
    l,c = map(int,input().split())
    m = []
    for i in range(l):
        m.append(list(map(int,input().split())))
        
    mai = 0
    be = bd = bc = bb = 0
    ce = cd = cc = cb = 0
    for i in range(l):
        for j in range(c):
            pont = m[i][j]
            
            #cima
            #print(pont)
            if i>0:
                if m[i-1][j]<pont:
                    bc = 1
                    if m[i-1][j] > mai:
                        mai = m[i-1][j]
            else:
                bc = -1
                
            #baixo
            
            if i<l-1:
                if m[i+1][j]<pont:
                    bb = 1
                    
                    if m[i+1][j] > mai:
                        mai = m[i+1][j]
            else:
                bb = -1
            #esquerda
            
            if j>0:
                if m[i][j-1]<pont:
                    be = 1
                    if m[i][j-1] > mai:
                        mai = m[i][j-1]
            else:
                be = -1
                
            #direita
            if j<c-1:
                if m[i][j+1]<pont:
                    bd = 1
                    if m[i][j+1] > mai:
                        mai = m[i][j+1]
                        
            else:
                bd = -1
            
            #print(pont)
            #print([bc,bb,be,bd])
            if 0 not in [bb,bc,be,bd]:
                m[i][j] = mai
                #print(m[i][j],'=',mai)
                
    
            bb =bc=be=bd = 0
            mai = 0
             
    #print()
    for i in m:
        print(*i,sep=' ')   
                
           
 
"""
1
5 4
92 74 31 74
74 92 17 7
31 17 92 3
74 7 3 92
7 31 1 1


74 74 31 31 
74 74 17  7 
31 17 17  3  
31  7  3  3 
 7  7  1  1
 
"""