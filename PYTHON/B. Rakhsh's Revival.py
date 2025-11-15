ct = int(input())

for w in range(ct):
    n,m,k = map(int,input().split())
    
    s = [int(x) for x in input()]
    c=p = 0
    
    if k == n:
        print(1)
        
    elif m == 1 and k == 1:
        for i in s:
            if i == 0:
                c +=1
        print(c)
    
    elif max(s) == 0:
        if n %2 == 0:
            print((n//m)-1)
        else:
            print((n//m))