n,s = map(int,input().split())

v = [str(x) for x in input()]
for i in range(s):
    
    c = 0
    for j in range(n-1):
        if c == 1:
            c = 0
            continue
        if v[j] == 'B' and v[j+1] == 'G':
            v[j],v[j+1] = v[j+1],v[j]
            c = 1
            
            
print(''.join(v))
        