for w in range(int(input())):
    v = [x for x in input()]
    
    c = 0
    s = 0
    for i in v:
        if v == 0:
            c+1
        s+=int(i)
            
    
    print(''.join(v))
    print('-----            >> ', (int(''.join(v))/s))
    print(s)
    print()