for w in range(int(input())):
    
    m = []
    v = []
    for i in range(8):
        m.append(input())
        
        
    for i in range(8):
        for j in range(8):
            if m[i][j] != '.':
                for k in range(i, 8-i-1):
                    if m[i][k] != '.':
                        v.append(m[i][k])
                        
                    else:
                        v.append('.')
                        break
    print(v)