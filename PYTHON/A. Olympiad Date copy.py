for w in range(int(input())):
    n = int(input())
    
    v = list(map(int,input().split()))
    
    s = [0,1,0,3,2,5]
    ind = 0
    
    for i in range(n):
        if len(s)>0:
            if v[i] in s:
                s.remove(v[i])
                ind = i
        else:
            break
        
    if len(s)>0:
        print(0)
    else: print(i+1)