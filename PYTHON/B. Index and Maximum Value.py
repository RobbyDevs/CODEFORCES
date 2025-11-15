#+ l r >> aumenta todos os elementos do indice
# 0 ate o fim do array em 1 para todo i<=r;

# l r >> diminui todos os elementos do indice
# 0 ate o fim do array em 1 para todo i<=r;


for w  in range(int(input())):
    
    n,m = map(int,input().split())
    
    v = list(map(int,input().split()))
    mai = max(v)
    imai = v.index(mai)+1
    #print(mai,imai)
    vr = []
    for i in range(m):
        op,l,r = map(str,input().split())
        
        #ind = int(ind)
        l = int(l)
        r = int(r)
        
        
        if (mai<=r and mai >=l):
            if (op == '+'):
                mai+=1
                
            else:
                mai-=1
        vr.append(mai)
    print(*vr,sep=' ')
    #print('^^^^^^^^^^')