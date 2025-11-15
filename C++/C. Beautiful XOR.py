for i in range(int(input())):
    a,b = map(int,input().split())
    
    if len(bin(a)[2:]) < len(bin(b)[2:]):
        print(-1)
        
    else:
        bina = bin(a)[2:]
        #print(bina)
        
        binx = ''
        for i in bina:
            if i == '1':
                binx+='0'
            else:
                binx+='1'
        print(2)
        x = int(binx,2)
        novoa = a^x
        print(x,novoa-b)
        #print("novo a:",novoa)
        #print(bina)
        
        #rint(int(bina)^int(binx))
        #print(int('111',2))