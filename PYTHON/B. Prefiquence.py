for w in range(int(input())):
    
    la,lb = map(int,input().split())
    va = input()
    
    vb = input()
    c = 0
    jj = 0
    for i in range(la):
        if jj >= lb:
            break
        for j in range(jj,lb):
            if vb[j] == va[i]:
                c+=1
                jj = j+1
                break
        else:
            break
    print(c)