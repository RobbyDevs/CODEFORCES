ct = int(input())

for _ in range(ct):
    ll,cc = map(int,input().split())
    cr = list(map(int,input().split()))

    s = []
    
    for i in range(0, 3, 2):
        c = cr[i]
        l = cr[i+1]
        a = 0
        
        if l == 1 or l == cc: #linha topo-base
            if c == 1 or c == ll:
                a = 2 # Esq-dir-Cima
                
            if c > 1 and c < ll:
                a = 3 #meio-cima
                
        elif l > 1 and l < cc: # meio
            if c == 1 or c == ll: 
                a =3
            if c > 1 and c < ll:
                a = 4
        s.append(a)
        
    print(min(s))
