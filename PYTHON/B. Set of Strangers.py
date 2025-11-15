for w in range(int(input())):
    
    n,m = map(int,input().split())
    
    
    ma = []
    va = []
    for i in range(n):
        ma.append(input())
        
    c=b=e=d=1
    val = 0
    for i in range(n):
        for j in range(m):
            
            if i >0 and i <n-1:
                
                if j > 0 and j < m-1:
                    if ma[i][j-1] == ma[i][j] or ma[i+1][j] == ma[i][j] or ma[i][j+1] == ma[i][j] or ma[i-1][j] == ma[i][j]:
                        va.append(ma[i][j])