for w in range(int(input())):
    
    v = [str(x) for x in input()]
    
    va = list(v)
    va = list(set(va))
    
    if len(va) == 1:
        print("NO")
    else:
        print('YES')
        va = []
        va = list(v)
        vs = list(sorted(v))
        #print(vs,va,sep='\n')
        if vs == va:
            
            vs.sort(reverse= True)
        
        print(*vs,sep='')
        