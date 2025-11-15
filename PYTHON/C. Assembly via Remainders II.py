for i in range(int(input())):
    
    l = int(input())
    
    v = list(map(int,input().split()))
    
    
    va = []
    va.append(100000)
    
    for i in range(len(v)):
        if v[i] < va[i-1]:
            va.append(va[i]+v[i])
        else:
            va.append(va[i]-v[i])
    
    
    print(*va, sep=' ')
    
    #for i in range(l-1):
        #print(f'mod {va[i+1]}%{va[i]}: {va[i+1]%va[i]}',end= ' | ')
    #print()
    #print()

