for w in range(int(input())):
    e = input()
    m = []

    for i in range(8):
        m.append(input())
        
    for j in range(8):
        if m[j] == 'RRRRRRRR':
            print('R')
            break
        
    else:
        for w in range(8):
            
            v = []
            for x in range(8):
                if m[x][w] == '.':
                    break
                v.append(m[x][w])
                
            if ''.join(v) == 'BBBBBBBB':
                print('B')
                break