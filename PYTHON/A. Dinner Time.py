for w in range(int(input())):
    
    n,m,p,q = map(int,input().split())

    propn = p/n
    propv = q/m
    
    print('>>',propn,propv)
    
    dif = propv/propn
    print(dif)