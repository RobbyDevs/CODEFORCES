for w in range(int(input())):
    n,k = map(int,input().split())
    
    v = input()
    zc = oc = 0
    for i in v:
        if i == '0':
            zc +=1
        else:
            oc+=1
            
    zc = zc//2 #n de pares zero
    oc = oc//2 #n de pares um
    
    #print('>>>',zc,oc)
    if abs(zc-oc)<=k:# se eu tiver pares o suficiente pra cancelar o excesso...
        if k%2 == (zc+oc)%2: #eles precisam ter a mesma paridade que k
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
