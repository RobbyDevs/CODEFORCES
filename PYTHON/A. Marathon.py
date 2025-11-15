for w in range(int(input())):
    
    v = list(map(int,input().split()))
    c = 0
    for i in v[1:]:
        if i > v[0]:
            c+=1
    print(c)