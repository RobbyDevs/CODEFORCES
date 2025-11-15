for w in range(int(input())):
    m = []
    n = int(input())
    s = [[] for x in range(n)]
    c = 0
    ma = [[x+1] for x in range(n)]
    
    for i in range(n):
        m.append([int(x) for x in input()])
       
        
    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                if j < i:
                    ma[i].append(j+1)
        

    
    ma.sort(key=lambda x: (len(x), -x[0] if x else float('-inf')))

    for i in range(len(ma)-1):
        print(ma[i][0],end=' ')
        
    print(ma[len(ma)-1][0]) 
    
"""1
3
000
001
010"""