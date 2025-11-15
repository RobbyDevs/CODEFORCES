    for w in range(int(input())):
        
        a,b = map(int,input().split())
        
        va = input()
        vb = input()
        c =0 
        while len(va) <= 50:
            
            if vb not in va:
                c+=1
                va = va + va
            else:

                break
            
        else:
            c = -1
        print(c)