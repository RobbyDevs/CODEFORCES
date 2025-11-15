n = int(input())

v = list(map(int,input().split()))
vo = sorted(v)
ma = vo[len(vo)-1]
sma = vo[len(vo)-2]

s = sum(v)
vb = []

for i in range(n):
    sa = s
    
    if v[i] != ma:
        sa -= v[i]
        
        if sa - ma == ma:
            vb.append(i+1)
    else:
        sa -= v[i]
        if sa - sma == sma:
            vb.append(i+1)
            
            
if len(vb)>0:
    print(len(vb))
    
    print(' '.join([str(x) for x in vb]))
else:
    print(0)
    print()