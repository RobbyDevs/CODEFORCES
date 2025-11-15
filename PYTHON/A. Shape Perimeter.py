for w in range(int(input())):
    
    n, a = map(int,input().split())
    
    m = []
    for i in range(n):
        m.append(list(map(int,input().split())))


    x = y= 0
    
    for i in range(len(m)):
        x += m[i][0]
        y += m[i][1]

    x,y = x+a-(m[0][1]),y+a-(m[0][0])

    s = ((x)*2)+((y)*2)
    print(s)
    