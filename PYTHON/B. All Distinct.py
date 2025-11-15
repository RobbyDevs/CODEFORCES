for w in range(int(input())):
    
    n = int(input())
    v = list(map(int,input().split()))

    va = []
    #vz = [0 for i in range(50)]
    vz = []
    
    for i in v:
        if i not in va:
            va.append(i)
            vz.append(0)
        else:
            try:
                vz[va.index(i)]+=1

            except IndexError:
                vz.append(0)
                vz[va.index(i)]+=1

    #print('>>>')
    
    if sum(vz) %2==0:
        print(len(va))
    else:
        print(len(va)-1)
