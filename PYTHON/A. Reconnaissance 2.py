n = int(input())

v = list(map(int,input().split()))

d = abs(v[0]-v[n-1])

ii,jj = 0,n-1


if n == 2:
    print(1,2)
    
else:
    for i in range(n-1):
        if abs(v[i+1]-v[i]) < d:
            d = abs(v[i+1]-v[i])
            ii,jj = i,i+1
    
    print(f'{ii+1} {jj+1}')
