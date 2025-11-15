from math import ceil

for w in range(int(input())):
    
    n,k = map(int,input().split())
    ni = c = s = 0

    ft = fr = r = 0
    
    ft = (n*(n+1))/2
    if n > k:
            
        fr = ((n-k)*(n-k+1))/2
    r = ft - fr
    
    if r %2 == 0:
        print('YES')
    else:
        print('NO') 