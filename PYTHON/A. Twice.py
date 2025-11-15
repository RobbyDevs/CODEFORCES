ct = int(input())

for i in range(ct):
    n = int(input())
    
    v = input().split()
    c=0
    while True:
        breaak = 0
        isclean = True
        nv = len(v)
        for i in range(nv):
            for j in range(nv):
                if i<j and v[i] == v[j]:
                    v.pop(j)
                    v.pop(i)
                    c+=1
                    isclean = False
                    breaak = 1
                    break
            if breaak == 1:
                break

        if isclean == True:
            break
                
    print(c)

