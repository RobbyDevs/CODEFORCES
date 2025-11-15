ct = int(input())

for i in range(ct):
    pf = 0
    f,r = map(int,input().split())
    p = list(map(int,input().split()))
    dif = r*2 - sum(p)

    for j in p:
        if j %2 == 0:
            pf += j
        elif j%2>0 and j>2:
            pf += j-1
            j=1
        if j == 1 and dif>=1:
            pf+=1
            dif = dif-1
    print(pf)
    
