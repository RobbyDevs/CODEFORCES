for w in range(int(input())):
    
    a,b,c,d = map(int,input().split())
    if a == b and a == c and a == d:
        print('YES')
    else:
        print('NO')