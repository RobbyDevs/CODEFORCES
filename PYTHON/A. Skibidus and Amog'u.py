for w in range(int(input())):
    
    v = [str(x) for x in input()]
    
    v.pop()
    v.pop()
    v.append('i')
    
    print(''.join(v))