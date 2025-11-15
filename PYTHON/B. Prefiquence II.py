for w in range(int(input())):
    la,lb = map(int,input().split())
    
    va = input()
    vb = input()
    
    ind = 0
    indi = 0
    for i in range(la):
        for j in range(ind,lb):
            if va[i] == vb[j]:
                ind = j+1
                indi = i+1
                break
        else:
            break
    
    
                
    print(indi)