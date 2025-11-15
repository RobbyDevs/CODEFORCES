for w in range(int(input())):
    
    v = [str(x) for x in input()]
    
    for i in range(len(v)-1):
        
        if v[i] == v[i+1]:
            print(1)
            break
    else:
        print(len(v))