for w in range(int(input())):
    
    m,a,b = map(int,input().split())
    x = y = 0
    v = input()
    c =0
    for _ in range(50):
        for i in v:
            if i == 'N':
                y +=1
            elif i == 'S':
                y-=1
            elif i == 'W':
                x -=1
            elif i == 'E':
                x +=1
            
            if a == x and b == y:
                print('YES')
                c = 1
                break
        if c == 1:
            break
        
    else:
        print('NO')
