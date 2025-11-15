import sys 
input = sys.stdin.readline


#0e | 1d
def BS(e,d,m):
    global vans
    global ind
    global flag

    m = (e+d)//2
    
    if (e+d)/2 > m:
        m+=1
    
    if vans[m]!=0:
        return
    
    vans[m] = ind
    ind-=1
    
    BS(m,d,m)#d
    BS(e,m,m)#e

    
    
    
    
    
    
    
def solve():
    n = int(input())
    l = n*2
    
    global ind
    ind = n-1
    global vans
    global flag
    flag = 0
    vans = [0]*l
    vans [0] = n
    vans[n] = n
    print(vans)
    
    e = 1
    d = n-1
    
    m = 0
    
    BS(e,d,m)
    print(vans)
    
    
    
    
for w in range(int(input())):
    solve()