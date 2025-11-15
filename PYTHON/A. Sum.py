for w in range(int(input())):
    
    v = list(map(int,input().split()))
    
    if max(v) == sum(v)-max(v):
        print('YES')
    else:
        print('NO')