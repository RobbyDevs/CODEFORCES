ct = int(input())

a = [x  for x in range(1,101)]

for _ in range(ct):
    n = int(input())
    vr = []
    v = []
    vn = []
            
    for i in range(1,101):
        
        r = a[i]%i
        
        if a not in vr:
            vr.append(r)
            
            vn.append([a[i],i])
    
    print(vr)
    print(vn)
    
    
"""                
                

    v = [str(x) for x in v]
    print(' '.join(v))"""