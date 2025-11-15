for w in range(int(input())):
    n,k = map(int,input().split())
    
    for i in (list(map(int,input().split()))):
        if i == k:
            print('YES')
            break
    else:
        print('NO')