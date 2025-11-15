for w in range(int(input())):
    
    v = list(int(x) for x in input())
    v.insert(0,1)
    #print(v)
    for i in range(5):
        if v[i] == 0:
            v[i] = 10
    c = 0
    for i in range(4):
        c = c + abs(v[i+1] - v[i]) +1
    print(c)