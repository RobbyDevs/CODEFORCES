for w in range(int(input())):
    n,k = map(int,input().split())
    
    v = list(map(int,input().split()))
    
    flag = 0
    ant = 0
    oc = 0
    add = 0
    ind = 0
    
                
    for i in range(n):
        if v[i] == 1:
            ind = i+k
            break
    
    if ind >=n:
        print('YES')
        continue

    #print(ind)
    for i in range(ind,n):
        if v[i] == 1:
            print('NO')
            break
    else:
        print('YES')     
    