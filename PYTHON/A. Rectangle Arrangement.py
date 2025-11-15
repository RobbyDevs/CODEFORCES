ct = int(input())

for i in range(ct):

    m = []
    n = int(input())
    for i in range(n):
        m.append(list(map(int,input().split())))
    
    mh=mw=pv = 0
    
#======================
    for k in range(n):
        if mw < m[k][0]:
            mw = m[k][0]
            
        if mh < m[k][1]:
            mh = m[k][1]
        
#=====================        
    pv = (2*mh) + (2*mw)

    print(pv)
