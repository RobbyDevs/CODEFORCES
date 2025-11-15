ct = int(input())

for w in range(ct):
    
    n = int(input())
    
    v = list(map(int,input().split()))
    st = True
    
    for i in range(n):
        
        
        if i<n-1:
            j = i+1
            if v[i] > v[j]:
                st = False
                break
    
    if st == False:
    
        if v[0] != min(v):
            print('NO')
        else:
            print('YES')
    else:
        print('YES')