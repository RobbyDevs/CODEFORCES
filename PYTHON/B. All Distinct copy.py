for w in range(int(input())):
    
    n = int(input())
    v = sorted(list(map(int,input().split())))
    print(v)
    va = []
    for i in range(1,n):
        if v[i]