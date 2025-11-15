for w in range(int(input())):
    
    l,r = map(int,input().split())
    L,R = map(int,input().split())
    l = l-1
    L = L-1

    area = 0
    if L == r or R == l:
        print(1)

    else:
        if L < l and R < r:
            area = R - L
            
        elif r < R and l < L:
            area = l - R
            
        elif L < l and r < R:
            area = r - l
        elif r < L and R < l:
            area = R - L
        elif L == l and R == r:
            area = R - L
        print(area)