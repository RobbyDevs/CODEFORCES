ct = int(input())

for w in range(ct):
    
    n,k = map(int,input().split())
    v = list(map(int,input().split()))
    org = True
    
    for i in range(n):
        j = i+1
        if i < n-1 and v[j]<v[i]:
            org = False
            break
    if org == True:
        print('YES')
    
    else:
        if k < 2:
            print('NO')

        else:
            print('YES')