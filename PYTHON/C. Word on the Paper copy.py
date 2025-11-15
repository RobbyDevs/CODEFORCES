for w in range(int(input())):
    
    m = []

    for i in range(8):
        a = input()
        
        v = [str(x) for x in a if x != "."]
        
        if v != []:
            a = v[0]
            m.append(a)
            
    print(''.join(m))