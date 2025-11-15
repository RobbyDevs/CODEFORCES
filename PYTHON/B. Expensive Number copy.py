for w in range(int(input())):
    v = [x for x in input()]
    
    z = 0
    s = 0
    lz = 0
    for i in range(len(v)-1):
        if v[i] == '0':
            z
            if v[i+1]!='0':
                lz +=1
            else:
                z+=1
    if v[-1] == '0':
        z+=1
        s+=int(i)             
        
    if lz==0:
        print(len(v)-1) 
           
    else:
        
        print(len(v)-(lz+z))
    