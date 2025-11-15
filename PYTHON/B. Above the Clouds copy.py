for w in range(int(input())):
    
    n = int(input())
    
    v = input()
    
    vf = [0 for x in range(97,123)]
    
    
    for i in v:
        vf[ord(i)-97]+=1
        

    if 3 in vf:
        print('YES')
        continue

    cont = 0
    dup = ''
    for i in range(len(vf)):
        if vf[i]>1:
            cont+=1
            dup = chr(i+97)
            
        if cont >1:
            break
    if cont>1:
        print('YES')
        continue    

        
    
    else:
        if v[0] == v[-1] and dup == v[0]:
            print('NO')
        else:
            print('YES')
    
    
#97-122